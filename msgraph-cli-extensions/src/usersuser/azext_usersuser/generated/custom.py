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


def usersuser_update(client,
                     user_id,
                     body):
    return client.update_user(user_id=user_id,
                              body=body)


def usersuser_delete(client,
                     user_id,
                     if_match=None):
    return client.delete_user(user_id=user_id,
                              if_match=if_match)


def usersuser_create_user(client,
                          body):
    return client.create_user(body=body)


def usersuser_get_user(client,
                       user_id,
                       select=None,
                       expand=None):
    return client.get_user(user_id=user_id,
                           select=select,
                           expand=expand)


def usersuser_list_user(client,
                        orderby=None,
                        select=None,
                        expand=None):
    return client.list_user(orderby=orderby,
                            select=select,
                            expand=expand)


def usersuser_update(client,
                     user_id,
                     id_=None,
                     availability=None,
                     activity=None):
    return client.update_presence(user_id=user_id,
                                  id=id_,
                                  availability=availability,
                                  activity=activity)


def usersuser_get_presence(client,
                           user_id,
                           select=None,
                           expand=None):
    return client.get_presence(user_id=user_id,
                               select=select,
                               expand=expand)
