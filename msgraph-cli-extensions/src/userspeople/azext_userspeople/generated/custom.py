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


def userspeople_update(client,
                       user_id,
                       person_id,
                       id_=None,
                       display_name=None,
                       given_name=None,
                       surname=None,
                       birthday=None,
                       person_notes=None,
                       is_favorite=None,
                       email_addresses=None,
                       phones=None,
                       postal_addresses=None,
                       websites=None,
                       title=None,
                       company_name=None,
                       yomi_company=None,
                       department=None,
                       office_location=None,
                       profession=None,
                       sources=None,
                       mailbox_type=None,
                       person_type=None,
                       user_principal_name=None):
    return client.update_person(user_id=user_id,
                                person_id=person_id,
                                id=id_,
                                display_name=display_name,
                                given_name=given_name,
                                surname=surname,
                                birthday=birthday,
                                person_notes=person_notes,
                                is_favorite=is_favorite,
                                email_addresses=email_addresses,
                                phones=phones,
                                postal_addresses=postal_addresses,
                                websites=websites,
                                title=title,
                                company_name=company_name,
                                yomi_company=yomi_company,
                                department=department,
                                office_location=office_location,
                                profession=profession,
                                sources=sources,
                                mailbox_type=mailbox_type,
                                person_type=person_type,
                                user_principal_name=user_principal_name)


def userspeople_create_person(client,
                              user_id,
                              id_=None,
                              display_name=None,
                              given_name=None,
                              surname=None,
                              birthday=None,
                              person_notes=None,
                              is_favorite=None,
                              email_addresses=None,
                              phones=None,
                              postal_addresses=None,
                              websites=None,
                              title=None,
                              company_name=None,
                              yomi_company=None,
                              department=None,
                              office_location=None,
                              profession=None,
                              sources=None,
                              mailbox_type=None,
                              person_type=None,
                              user_principal_name=None):
    return client.create_person(user_id=user_id,
                                id=id_,
                                display_name=display_name,
                                given_name=given_name,
                                surname=surname,
                                birthday=birthday,
                                person_notes=person_notes,
                                is_favorite=is_favorite,
                                email_addresses=email_addresses,
                                phones=phones,
                                postal_addresses=postal_addresses,
                                websites=websites,
                                title=title,
                                company_name=company_name,
                                yomi_company=yomi_company,
                                department=department,
                                office_location=office_location,
                                profession=profession,
                                sources=sources,
                                mailbox_type=mailbox_type,
                                person_type=person_type,
                                user_principal_name=user_principal_name)


def userspeople_get_person(client,
                           user_id,
                           person_id,
                           select=None,
                           expand=None):
    return client.get_person(user_id=user_id,
                             person_id=person_id,
                             select=select,
                             expand=expand)


def userspeople_list_person(client,
                            user_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_person(user_id=user_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)
