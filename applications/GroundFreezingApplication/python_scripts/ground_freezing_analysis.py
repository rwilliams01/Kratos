import time as timer
import os

import KratosMultiphysics as Kratos
import KratosMultiphysics.LinearSolversApplication
import KratosMultiphysics.GroundFreezingApplication

from KratosMultiphysics.analysis_stage import AnalysisStage

from importlib import import_module

class GroundFreeezingAnalysis(AnalysisStage):
    '''Main script for poromechanics simulations.'''

    def __init__(self,model,parameters):
        # Creating solver and model part and adding variables
        super(GroundFreeezingAnalysis,self).__init__(model,parameters)

    def Initialize(self):
        super(GroundFreeezingAnalysis,self).Initialize()

    def OutputSolutionStep(self):
        super(GroundFreeezingAnalysis,self).OutputSolutionStep()

    def Finalize(self):
        super(GroundFreeezingAnalysis,self).Finalize()

    #### Internal functions ####
    
#    def _CreateSolver(self):
#        python_module_name = "KratosMultiphysics.GroundFreezingApplication"
#        full_module_name = python_module_name + "." + self.project_parameters["solver_settings"]["solver_type"].GetString()
#        solver_module = import_module(full_module_name)
#        solver = solver_module.CreateSolver(self.model, self.project_parameters["solver_settings"])
#        return solver

#    def _GetSimulationName(self):
#        return "Ground Freezing Analysis"


if __name__ == '__main__':
    from sys import argv

    if len(argv) > 2:
        err_msg =  'Too many input arguments!\n'
        err_msg += 'Use this script in the following way:\n'
        err_msg += '- With default parameter file (assumed to be called "ProjectParameters.json"):\n'
        err_msg += '    "python poromechanics_analysis.py"\n'
        err_msg += '- With custom parameter file:\n'
        err_msg += '    "python poromechanics_analysis.py <my-parameter-file>.json"\n'
        raise Exception(err_msg)

    if len(argv) == 2: # ProjectParameters is being passed from outside
        parameter_file_name = argv[1]
    else: # using default name
        parameter_file_name = "ProjectParameters.json"

    with open(parameter_file_name,'r') as parameter_file:
        parameters = Kratos.Parameters(parameter_file.read())

    model = Kratos.Model()
    simulation = GroundFreeezingAnalysis(model,parameters)
    simulation.Run()
