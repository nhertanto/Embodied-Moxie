# *************************************************************************************
# README:
# This is the "Pattern Testing Tool". In this tool, users are able to test
#   their patterns, a phrase Moxie looks for when speaking to it. This empowers
#   designers to anticipate anything a child may say to Moxie and have Moxie respond
#   accordingly!
# NOTE:
#    I co-developed this tool with my teammates! My contributions will be shown below
#    in comments with Niken - 
#    My main contribution to this is allowing users to test their patterns quickly
#    in "interactive mode" (rather than using a CSV sheet for bulk testing)
# *************************************************************************************

from cgi import test
from ctypes import sizeof
from dataclasses import field
from logging import exception
from pybrain_wrapper import PybrainWrapper
from tabulate import tabulate
import os
import pathlib
import re
import csv
import argparse
import subprocess
import io
import readline
import selectors
import sys

from typing import List, Dict, Union, Any

from pathlib import Path

from threading import Thread

USER_CS_LOG_PATH = "chatscript/USERS/log-user.txt"

# Niken - I added an Intro Message to tell the users the
#         commands they can write in this tool
INTRO_MESSAGE = """
****************  Interactive Pattern Testing *****************

Here you can create and test your patterns!

Please type either of the following commands in this format:
    * :testpattern (pattern) pattern sample
    * :word word
    * :down ~concept
    * :up ~concept
    * help
    * exit

***************************************************************  
    """

# Niken - I wrote descriptions of all the commands if asked
HELP_MESSAGE = """
DESCRIPTION:
    * :testpattern - This allows you to test your pattern and a
            sample phrase against it! If your sample phrase matches your
            pattern, then it would say Match: TRUE, if not, Match: FALSE
    * :word - This command displays info about the given word, such as its
            canonical form, as well as any concepts that word may be a part of.
    * :down - This command lets you look inside a concept. Words inside a concept
            tend to be synonyms (ex. ~greeting --> hello, hi, etc), or 
            grouped together (ex. ~fruit --> apple, banana, etc)
    * :up - This command allows you to see what other higher-level concepts that
            your concept may be a part of. (EX. ~pet_animals is a part of ~animals, etc
    NOTE: For more info on making patterns, please follow this link:
            https://embodied.atlassian.net/wiki/spaces/CBP/pages/29524050/Patterns
    NOTE: For more info on the Pattern Testing Tool, please follow this link:
            https://embodied.atlassian.net/wiki/spaces/CBP/pages/1950842883/Pattern+Testing+Tool
    """


class TestPatternInstance():
    
    command: str
    pattern: str
    sample: str
    expected_outcome: str
    actual_outcome: str
    message: str

    def __init__(self, pattern, sample, expected_outcome):
        self.pattern = pattern
        self.sample = sample
        self.expected_outcome = expected_outcome
        self.actual_outcome = ""
        self.message = ""

    def update_instance(self, actual_outcome, message):
        self.actual_outcome = actual_outcome
        self.message = message

    def return_instance(self):
        return[self.pattern, self.sample, self.expected_outcome, self.actual_outcome, self.message]


def get_inputs_from_csv(inputs_csv):
    # reading csv file
    with open(inputs_csv, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.DictReader(csvfile)

        test_pattern_inputs: List[TestPatternInstance]
        test_pattern_inputs = []
        for row in csvreader:
            if row['expected_outcome'] not in ['True', 'False']:
                print(row)
                raise Exception("Expected outcome has to be 'True' or 'False")
                # strip() is needed
            if row['pattern'][0] != '(' or row['pattern'][-1] != ')':
                print(row)
                raise Exception("pattern should be enclosed in parenthesis ()")
            input = TestPatternInstance(row['pattern'], row['sample'], row['expected_outcome'])
            test_pattern_inputs.append(input)

        return test_pattern_inputs


def test_pattern(engine, test_pattern_instance, failed_instances):
    match, message = engine.TestPattern(test_pattern_instance.pattern, test_pattern_instance.sample)
    test_pattern_instance.update_instance(str(match), message)
    if str(match) != test_pattern_instance.expected_outcome:
        failed_instances.append(test_pattern_instance)
    return test_pattern_instance, failed_instances


def write_to_output_csv(test_pattern_output, all_instances):
    with open(test_pattern_output, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['pattern','sample','expected_outcome','actual_outcome','message'])
        for instance in all_instances:
            csvwriter.writerow(instance.return_instance())


def print_failed_instances(failed_instances):
    print('\n\n*******        FAILING INSTANCES        ********')
    for instance in failed_instances:
        print(instance.return_instance())
    print('\n')
  

# Niken - This definition utilizes Chatscript's ability to read and decipher patterns.
def get_last_log(command:str="", user_input:str="", sample:str=""):
    user_command = command + user_input + sample
    chat_engine.RunVolley(user_command)
    path = pathlib.Path(USER_CS_LOG_PATH)
    if not path.exists():
        return False
    with open(path, "rb") as file:
        try:
            decoded_file = file.read().decode()
            if 'Command:' in decoded_file:
                idx = decoded_file.rfind('Command:')
                print('\n')
                print(decoded_file[idx:])
        except OSError:
            file.seek(0)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Pattern validation')
    parser.add_argument("-i", dest="interactive", default=False, action="store_true",
                        help="test pattern interactively on the terminal")
    parser.add_argument("-input", dest="test_pattern_input", metavar='csv', type=str, help='csv with patterns, samples and expected outcomes')
    parser.add_argument("-output", dest="test_pattern_output", metavar='csv', type=str, help='output csv file test pattern results')

    args = parser.parse_args()

    interactive: bool = args.interactive
    sampleNeeded: bool

    chat_engine = PybrainWrapper()
    chat_engine.setup_engine()
    chat_engine.clear_user_log()


    # Niken - While in interactive mode, users are able to type in their command and test their patterns!
    if interactive:
        print(tabulate([[INTRO_MESSAGE]], tablefmt='grid'))
        while interactive:
            command = input('Type in your command: ')
            if re.fullmatch(r'^\s*help\s*$',command, re.I):
                print(tabulate([[HELP_MESSAGE]], tablefmt='grid'))
            elif re.fullmatch(r'^\s*exit\s*$',command, re.I):
                print('\nBye bye I will miss you! ^_^')
                break
            elif re.fullmatch(r'^\s*:(testpattern|word|up|down)\s?.*', command, re.I):
                get_last_log(command)
            else:
                print('\n\u001b[31m:( I cannot understand your odd combination of letters and words. Please try again, or type help!\u001b[0m')
            print('\n***************************************************************\n')

    else:

        test_pattern_inputs = get_inputs_from_csv(args.test_pattern_input)

        failed_instances = []
        all_instances = []

        for input in test_pattern_inputs:
            test_pattern_instance, updated_failed_instances = test_pattern(chat_engine, input, failed_instances)
            all_instances.append(test_pattern_instance)
            failed_instances = updated_failed_instances

        write_to_output_csv(args.test_pattern_output, all_instances)
        print_failed_instances(failed_instances)
