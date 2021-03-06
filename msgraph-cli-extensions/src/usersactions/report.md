# Azure CLI Module Creation Report

### usersactions accept

accept a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|accept|accept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions assign-license

assign-license a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|assign-license|assignLicense|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--add-licenses**|array||add_licenses|addLicenses|
|**--remove-licenses**|array||remove_licenses|removeLicenses|

### usersactions bypass-activation-lock

bypass-activation-lock a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|bypass-activation-lock|bypassActivationLock|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions change-password

change-password a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|change-password|changePassword|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--current-password**|string||current_password|currentPassword|
|**--new-password**|string||new_password|newPassword|

### usersactions check-member-group

check-member-group a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-group|checkMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--group-ids**|array||group_ids|groupIds|

### usersactions check-member-object

check-member-object a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|check-member-object|checkMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--ids**|array||ids|ids|

### usersactions clean-window-device

clean-window-device a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|clean-window-device|cleanWindowsDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--keep-user-data**|boolean||keep_user_data|keepUserData|

### usersactions copy

copy a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy|copy|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions copy-notebook

copy-notebook a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.sections.parentSectionGroup.parentNotebook|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-notebook|copyNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--notebook-folder**|string||notebook_folder|notebookFolder|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions copy-to-notebook

copy-to-notebook a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-notebook|copyToNotebook|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions copy-to-section

copy-to-section a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section|copyToSection|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions copy-to-section-group

copy-to-section-group a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.sections.parentSectionGroup.sections|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|copy-to-section-group|copyToSectionGroup|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-section-id1**|string|key: id of onenoteSection|onenote_section_id1|onenoteSection-id1|
|**--id**|string||id|id|
|**--group-id**|string||group_id|groupId|
|**--rename-as**|string||rename_as|renameAs|
|**--site-collection-id**|string||site_collection_id|siteCollectionId|
|**--site-id**|string||site_id|siteId|

### usersactions create-forward

create-forward a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-forward|createForward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions create-or-get

create-or-get a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onlineMeetings|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-or-get|createOrGet|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--chat-info**|object|chatInfo|chat_info|chatInfo|
|**--end-date-time**|date-time||end_date_time|endDateTime|
|**--external-id**|string||external_id|externalId|
|**--start-date-time**|date-time||start_date_time|startDateTime|
|**--subject**|string||subject|subject|
|**--participants-attendees**|array||attendees|attendees|
|**--participants-organizer**|object|meetingParticipantInfo|organizer|organizer|

### usersactions create-reply

create-reply a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply|createReply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions create-reply-all

create-reply-all a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-reply-all|createReplyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions create-upload-session

create-upload-session a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages.attachments|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|create-upload-session|createUploadSession|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--attachment-item**|object|attachmentItem|attachment_item|AttachmentItem|

### usersactions decline

decline a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|decline|decline|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions delete-user-from-shared-apple-device

delete-user-from-shared-apple-device a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|delete-user-from-shared-apple-device|deleteUserFromSharedAppleDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--user-principal-name**|string||user_principal_name|userPrincipalName|

### usersactions disable-lost-mode

disable-lost-mode a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|disable-lost-mode|disableLostMode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions dismiss-reminder

dismiss-reminder a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|dismiss-reminder|dismissReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|

### usersactions export-personal-data

export-personal-data a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|export-personal-data|exportPersonalData|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--storage-location**|string||storage_location|storageLocation|

### usersactions find-meeting-time

find-meeting-time a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|find-meeting-time|findMeetingTimes|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--body**|object|Action parameters|body|body|

### usersactions forward

forward a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|forward|forward|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--to-recipients**|array||to_recipients|ToRecipients|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|microsoft_graph_message_to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions get-available-extension-property

get-available-extension-property a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-available-extension-property|getAvailableExtensionProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--is-synced-from-on-premises**|boolean||is_synced_from_on_premises|isSyncedFromOnPremises|

### usersactions get-by-id

get-by-id a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-by-id|getByIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--ids**|array||ids|ids|
|**--types**|array||types|types|

### usersactions get-mail-tip

get-mail-tip a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-mail-tip|getMailTips|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--email-addresses**|array||email_addresses|EmailAddresses|
|**--mail-tips-options**|choice||mail_tips_options|MailTipsOptions|

### usersactions get-member-group

get-member-group a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-group|getMemberGroups|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### usersactions get-member-object

get-member-object a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-member-object|getMemberObjects|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--security-enabled-only**|boolean||security_enabled_only|securityEnabledOnly|

### usersactions get-notebook-from-web-url

get-notebook-from-web-url a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.notebooks|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-notebook-from-web-url|getNotebookFromWebUrl|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--web-url**|string||web_url|webUrl|

### usersactions get-schedule

get-schedule a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events.calendar|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|get-schedule|getSchedule|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--schedules**|array||schedules|Schedules|
|**--end-time**|object|dateTimeTimeZone|end_time|EndTime|
|**--start-time**|object|dateTimeTimeZone|start_time|StartTime|
|**--availability-view-interval**|integer||availability_view_interval|AvailabilityViewInterval|

### usersactions locate-device

locate-device a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|locate-device|locateDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions logout-shared-apple-device-active-user

logout-shared-apple-device-active-user a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|logout-shared-apple-device-active-user|logoutSharedAppleDeviceActiveUser|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions move

move a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|move|move|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--destination-id**|string||destination_id|DestinationId|

### usersactions onenote-patch-content

onenote-patch-content a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.onenote.sections.pages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|onenote-patch-content|onenotePatchContent|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--onenote-section-id**|string|key: id of onenoteSection|onenote_section_id|onenoteSection-id|
|**--onenote-page-id**|string|key: id of onenotePage|onenote_page_id|onenotePage-id|
|**--commands**|array||commands|commands|

### usersactions reboot-now

reboot-now a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reboot-now|rebootNow|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions recover-passcode

recover-passcode a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|recover-passcode|recoverPasscode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions remote-lock

remote-lock a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remote-lock|remoteLock|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions remove-all-device-from-management

remove-all-device-from-management a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|remove-all-device-from-management|removeAllDevicesFromManagement|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions reply

reply a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply|reply|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions reply-all

reply-all a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reply-all|replyAll|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|
|**--comment**|string||comment|Comment|
|**--id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions reprocess-license-assignment

reprocess-license-assignment a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reprocess-license-assignment|reprocessLicenseAssignment|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions request-remote-assistance

request-remote-assistance a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|request-remote-assistance|requestRemoteAssistance|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions reset-passcode

reset-passcode a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|reset-passcode|resetPasscode|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions restore

restore a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|restore|restore|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions retire

retire a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|retire|retire|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions revoke-sign-in-session

revoke-sign-in-session a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|revoke-sign-in-session|revokeSignInSessions|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|

### usersactions send

send a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.messages|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send|send|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--message-id**|string|key: id of message|message_id|message-id|

### usersactions send-mail

send-mail a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|send-mail|sendMail|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--save-to-sent-items**|boolean||save_to_sent_items|SaveToSentItems|
|**--message-id**|string|Read-only.|id|id|
|**--message-categories**|array|The categories associated with the item|categories|categories|
|**--message-change-key**|string|Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.|change_key|changeKey|
|**--message-created-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|created_date_time|createdDateTime|
|**--message-last-modified-date-time**|date-time|The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'|last_modified_date_time|lastModifiedDateTime|
|**--message-bcc-recipients**|array|The Bcc: recipients for the message.|bcc_recipients|bccRecipients|
|**--message-body**|object|itemBody|body|body|
|**--message-body-preview**|string|The first 255 characters of the message body. It is in text format.|body_preview|bodyPreview|
|**--message-cc-recipients**|array|The Cc: recipients for the message.|cc_recipients|ccRecipients|
|**--message-conversation-id**|string|The ID of the conversation the email belongs to.|conversation_id|conversationId|
|**--message-conversation-index**|byte-array|Indicates the position of the message within the conversation.|conversation_index|conversationIndex|
|**--message-flag**|object|followupFlag|flag|flag|
|**--message-from**|object|recipient|from|from|
|**--message-has-attachments**|boolean|Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as :code:`<IMG src='cid:image001.jpg@01D26CD8.6C05F070'>`.|has_attachments|hasAttachments|
|**--message-importance**|choice||importance|importance|
|**--message-inference-classification**|choice||inference_classification|inferenceClassification|
|**--message-internet-message-headers**|array|A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.|internet_message_headers|internetMessageHeaders|
|**--message-internet-message-id**|string|The message ID in the format specified by RFC2822.|internet_message_id|internetMessageId|
|**--message-is-delivery-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_delivery_receipt_requested|isDeliveryReceiptRequested|
|**--message-is-draft**|boolean|Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.|is_draft|isDraft|
|**--message-is-read**|boolean|Indicates whether the message has been read.|is_read|isRead|
|**--message-is-read-receipt-requested**|boolean|Indicates whether a read receipt is requested for the message.|is_read_receipt_requested|isReadReceiptRequested|
|**--message-parent-folder-id**|string|The unique identifier for the message's parent mailFolder.|parent_folder_id|parentFolderId|
|**--message-received-date-time**|date-time|The date and time the message was received.|received_date_time|receivedDateTime|
|**--message-reply-to**|array|The email addresses to use when replying.|reply_to|replyTo|
|**--message-sender**|object|recipient|sender|sender|
|**--message-sent-date-time**|date-time|The date and time the message was sent.|sent_date_time|sentDateTime|
|**--message-subject**|string|The subject of the message.|subject|subject|
|**--message-to-recipients**|array|The To: recipients for the message.|to_recipients|toRecipients|
|**--message-unique-body**|object|itemBody|unique_body|uniqueBody|
|**--message-web-link**|string|The URL to open the message in Outlook Web App.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, then the browser will show the message in the Outlook Web App review pane.The message will open in the browser if you are logged in to your mailbox via Outlook Web App. You will be prompted to login if you are not already logged in with the browser.This URL can be accessed from within an iFrame.|web_link|webLink|
|**--message-attachments**|array|The fileAttachment and itemAttachment attachments for the message.|attachments|attachments|
|**--message-extensions**|array|The collection of open extensions defined for the message. Nullable.|extensions|extensions|
|**--message-multi-value-extended-properties**|array|The collection of multi-value extended properties defined for the message. Nullable.|multi_value_extended_properties|multiValueExtendedProperties|
|**--message-single-value-extended-properties**|array|The collection of single-value extended properties defined for the message. Nullable.|single_value_extended_properties|singleValueExtendedProperties|

### usersactions shut-down

shut-down a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|shut-down|shutDown|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions snooze-reminder

snooze-reminder a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|snooze-reminder|snoozeReminder|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--new-reminder-time**|object|dateTimeTimeZone|new_reminder_time|NewReminderTime|

### usersactions sync-device

sync-device a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|sync-device|syncDevice|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions tentatively-accept

tentatively-accept a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.events|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|tentatively-accept|tentativelyAccept|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--event-id**|string|key: id of event|event_id|event-id|
|**--comment**|string||comment|Comment|
|**--send-response**|boolean||send_response|SendResponse|

### usersactions translate-exchange-id

translate-exchange-id a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|translate-exchange-id|translateExchangeIds|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--input-ids**|array||input_ids|InputIds|
|**--target-id-type**|choice||target_id_type|TargetIdType|
|**--source-id-type**|choice||source_id_type|SourceIdType|

### usersactions update-window-device-account

update-window-device-account a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|update-window-device-account|updateWindowsDeviceAccount|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--update-windows-device-account-action-parameter-calendar-sync-enabled**|boolean|Not yet documented|calendar_sync_enabled|calendarSyncEnabled|
|**--update-windows-device-account-action-parameter-device-account-email**|string|Not yet documented|device_account_email|deviceAccountEmail|
|**--update-windows-device-account-action-parameter-exchange-server**|string|Not yet documented|exchange_server|exchangeServer|
|**--update-windows-device-account-action-parameter-password-rotation-enabled**|boolean|Not yet documented|password_rotation_enabled|passwordRotationEnabled|
|**--update-windows-device-account-action-parameter-session-initiation-protocal-address**|string|Not yet documented|session_initiation_protocal_address|sessionInitiationProtocalAddress|
|**--update-windows-device-account-action-parameter-device-account-password**|string|Not yet documented|password|password|

### usersactions validate-property

validate-property a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|validate-property|validateProperties|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--entity-type**|string||entity_type|entityType|
|**--display-name**|string||display_name|displayName|
|**--mail-nickname**|string||mail_nickname|mailNickname|
|**--on-behalf-of-user-id**|uuid||on_behalf_of_user_id|onBehalfOfUserId|

### usersactions window-defender-scan

window-defender-scan a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|window-defender-scan|windowsDefenderScan|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--quick-scan**|boolean||quick_scan|quickScan|

### usersactions window-defender-update-signature

window-defender-update-signature a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|window-defender-update-signature|windowsDefenderUpdateSignatures|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|

### usersactions wipe

wipe a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users.managedDevices|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|wipe|wipe|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--managed-device-id**|string|key: id of managedDevice|managed_device_id|managedDevice-id|
|**--keep-enrollment-data**|boolean||keep_enrollment_data|keepEnrollmentData|
|**--keep-user-data**|boolean||keep_user_data|keepUserData|
|**--mac-os-unlock-code**|string||mac_os_unlock_code|macOsUnlockCode|

### usersactions wipe-managed-app-registration-by-device-tag

wipe-managed-app-registration-by-device-tag a usersactions.

#### Command group
|Name (az)|Swagger name|
|---------|------------|
|usersactions|users|

#### Methods
|Name (az)|Swagger name|
|---------|------------|
|wipe-managed-app-registration-by-device-tag|wipeManagedAppRegistrationsByDeviceTag|

#### Parameters
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--user-id**|string|key: id of user|user_id|user-id|
|**--device-tag**|string||device_tag|deviceTag|
