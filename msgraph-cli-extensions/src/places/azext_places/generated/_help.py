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


helps['places'] = """
    type: group
    short-summary: places
"""

helps['places update'] = """
    type: command
    short-summary: Update entity in places
    parameters:
      - name: --geo-coordinates
        short-summary: outlookGeoCoordinates
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX accuracy=XX altitude-accuracy=XX

            altitude: The altitude of the location.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude-accuracy: The accuracy of the altitude.
      - name: --address
        short-summary: physicalAddress
        long-summary: |
            Usage: --address type=XX post-office-box=XX street=XX city=XX state=XX country-or-region=XX postal-code=XX

            street: The street.
            city: The city.
            state: The state.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
"""

helps['places delete'] = """
    type: command
    short-summary: Delete entity from places
"""

helps['places create-place'] = """
    type: command
    short-summary: Add new entity to places
    parameters:
      - name: --geo-coordinates
        short-summary: outlookGeoCoordinates
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX accuracy=XX altitude-accuracy=XX

            altitude: The altitude of the location.
            latitude: The latitude of the location.
            longitude: The longitude of the location.
            accuracy: The accuracy of the latitude and longitude. As an example, the accuracy can be measured in \
meters, such as the latitude and longitude are accurate to within 50 meters.
            altitude-accuracy: The accuracy of the altitude.
      - name: --address
        short-summary: physicalAddress
        long-summary: |
            Usage: --address type=XX post-office-box=XX street=XX city=XX state=XX country-or-region=XX postal-code=XX

            street: The street.
            city: The city.
            state: The state.
            country-or-region: The country or region. It's a free-format string value, for example, 'United States'.
            postal-code: The postal code.
"""

helps['places get-place'] = """
    type: command
    short-summary: Get entity from places by key
"""

helps['places list-place'] = """
    type: command
    short-summary: Get entities from places
"""
