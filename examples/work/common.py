# -*- coding: utf-8 -*-

from aiida.work.workfunction import workfunction
from aiida.work.run import run
from aiida.orm import DataFactory
from aiida.orm.calculation.job.quantumespresso.pw import PwCalculation
from aiida.orm.code import Code


__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__authors__ = "The AiiDA team."
__version__ = "0.7.1"

def get_pseudos(structure, family_name):
    """
    Set the pseudo to use for all atomic kinds, picking pseudos from the
    family with name family_name.

    :note: The structure must already be set.

    :param family_name: the name of the group containing the pseudos
    """
    from collections import defaultdict
    from aiida.orm.data.upf import get_pseudos_from_structure

    # A dict {kind_name: pseudo_object}
    kind_pseudo_dict = get_pseudos_from_structure(structure, family_name)

    # We have to group the species by pseudo, I use the pseudo PK
    # pseudo_dict will just map PK->pseudo_object
    pseudo_dict = {}
    # Will contain a list of all species of the pseudo with given PK
    pseudo_species = defaultdict(list)

    for kindname, pseudo in kind_pseudo_dict.iteritems():
        pseudo_dict[pseudo.pk] = pseudo
        pseudo_species[pseudo.pk].append(kindname)

    pseudos = {}
    for pseudo_pk in pseudo_dict:
        pseudo = pseudo_dict[pseudo_pk]
        kinds = pseudo_species[pseudo_pk]
        for kind in kinds:
            pseudos[kind] = pseudo

    return pseudos


def generate_scf_input_params(structure, codename, pseudo_family):
    # The inputs
    inputs = PwCalculation.process().get_inputs_template()

    # The structure
    inputs.structure = structure

    inputs.code = Code.get_from_string(codename.value)
    inputs._options.resources = {"num_machines": 1}
    inputs._options.max_wallclock_seconds = 30 * 60

    # Kpoints
    KpointsData = DataFactory("array.kpoints")
    kpoints = KpointsData()
    kpoints_mesh = 2
    kpoints.set_kpoints_mesh([kpoints_mesh, kpoints_mesh, kpoints_mesh])
    inputs.kpoints = kpoints

    # Calculation parameters
    parameters_dict = {
        "CONTROL": {"calculation": "scf",
                    "tstress": True,  #  Important that this stays to get stress
                    "tprnfor": True,},
        "SYSTEM": {"ecutwfc": 30.,
                   "ecutrho": 200.,},
        "ELECTRONS": {"conv_thr": 1.e-6,}
    }
    ParameterData = DataFactory("parameter")
    inputs.parameters = ParameterData(dict=parameters_dict)

    # Pseudopotentials
    inputs.pseudo = get_pseudos(structure, str(pseudo_family))

    return inputs

@workfunction
def run_scf(structure, codename, pseudo_family):
    JobCalc = PwCalculation.process()
    inputs = generate_scf_input_params(structure, codename, pseudo_family)
    return run(JobCalc, **inputs)

