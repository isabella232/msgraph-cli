# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['notification'] = """
    type: group
    short-summary: notification
"""

helps['notification create-notification'] = """
    type: command
    short-summary: "Create new navigation property to notifications for users"
    parameters:
      - name: --target-policy
        short-summary: "targetPolicyEndpoints"
        long-summary: |
            Usage: --target-policy platform-types=XX

      - name: --payload-visual-content
        short-summary: "visualProperties"
        long-summary: |
            Usage: --payload-visual-content title=XX body=XX

"""

helps['notification get-notification'] = """
    type: command
    short-summary: "Get notifications from users"
"""

helps['notification list-notification'] = """
    type: command
    short-summary: "Get notifications from users"
"""

helps['notification update-notification'] = """
    type: command
    short-summary: "Update the navigation property notifications in users"
    parameters:
      - name: --target-policy
        short-summary: "targetPolicyEndpoints"
        long-summary: |
            Usage: --target-policy platform-types=XX

      - name: --payload-visual-content
        short-summary: "visualProperties"
        long-summary: |
            Usage: --payload-visual-content title=XX body=XX

"""
