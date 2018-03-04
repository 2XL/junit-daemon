#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import json
import os

from invoke import task
from pipeline import executor


@task
def clean(ctx):
    """ Cleans up generated files, clean all files in source
    """
    # cleanup migration
    ctx.run('rm -rf src/*')
    ctx.run('rm -rf out/*')
    ctx.run('rm -rf tests/*')
    ctx.run('rm -rf reports/*')


@task(pre=[clean], post=[])
def build(ctx, code=None, language='java', fixture=None, test='junit', case='answer'):
    """Provision the project with the provided payload
         # -c   answer submitted by the user        - expect it to be k/v = relative path to `project`
         # -t   test framework                      `default: pytest` # dummy field
         # -f   assertion_fixture, code             - expect it to be k/v = relative path to `project`, json encoded
         # -l   java                                `default: java` # dummy field
    :param ctx:
    :param code:
    :param language:
    :param fixture:
    :param test:
    :param case:
    :return:
    """
    # print code

# if __name__ == "__main__":
#     case = 'answer'
#     code = None
#     fixture = None

    data = None



    if code is None:
        # load default bootstrap source for demo
        with open('data/data.json', 'r') as file_stream:
            challenge = json.load(file_stream)
            code_submission = '\n'.join(challenge['challenge'][case]['files'])
            valid_assertion = '\n'.join(challenge['challenge']['valid_assertion']['files'])
            data = '\n'.join([code_submission, valid_assertion])
    else:
        data = code

    if fixture is not None:
        data = fixture

    print data
    submission = executor.PipelineExecutor()
    submission.load_queue_from_submission(code=data)
    # submission.list_queue()
    submission.apply_queue()
    pass
