#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__version__ = "0.7.1"
__authors__ = "The AiiDA team."

from aiida.backends.utils import load_dbenv, is_dbenv_loaded

if not is_dbenv_loaded():
    load_dbenv()

import time
from aiida.orm.data.base import Int
from aiida.work.run import async, run, submit
from aiida.work.workfunction import workfunction
from aiida.work.workchain import (WorkChain, ToContext)


@workfunction
def f1(inp=None):
    p2 = async(long_running, a=inp)
    a = 1  # Do some work...
    r2 = p2.result()
    print("a={}".format(a))
    print("r2={}".format(r2))

    return {'r1': r2['r2']}


@workfunction
def long_running(a):
    time.sleep(2)
    return {'r2': a}


class F1(WorkChain):
    @classmethod
    def define(cls, spec):
        super(F1, cls).define(spec)

        spec.dynamic_input()
        spec.dynamic_output()
        spec.outline(cls.s1, cls.s2)

    def s1(self):
        p2 = async(LongRunning, a=self.inputs.inp)
        self.ctx.a = 1  # Do some work...
        return ToContext(r2=p2.pid)

    def s2(self):
        print("a={}".format(self.ctx.a))
        print("r2={}".format(self.ctx.r2))

        self.out("r1", self.ctx.r2['r2'])


class LongRunning(WorkChain):
    @classmethod
    def define(cls, spec):
        super(LongRunning, cls).define(spec)

        spec.dynamic_input()
        spec.dynamic_output()
        spec.outline(cls.s1)

    def s1(self):
        time.sleep(2)
        self.out("r2", self.inputs.a)


class F1WaitFor(WorkChain):
    @classmethod
    def define(cls, spec):
        super(F1WaitFor, cls).define(spec)

        spec.dynamic_input()
        spec.dynamic_output()
        spec.outline(cls.s1, cls.s2)

    def s1(self):
        p2 = async(long_running, a=self.inputs.inp)
        self.ctx.a = 1
        self.ctx.r2 = p2.result()

    def s2(self):
        print("a={}".format(self.ctx.a))
        print("r2={}".format(self.ctx.r2))

        self.out("r1", self.ctx.r2['r2'])


if __name__ == '__main__':
    five = Int(5)

    r1 = f1(five)
    run(F1, inp=five)
    R1 = run(F1WaitFor, inp=five)['r1']

