<h3>

:table_name="ActionSequence"
:description="   This table holds the name and Id number of action sets that are created under the Infusionsoft Logo &gt; Marketing Settings &gt; Action Sets within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="TemplateName"
      :type="String"
      :access="Read"

      :name="VisibleToTheseUsers"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="AffResource"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Notes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ProgramIds"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ResourceHREF"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ResourceHTML"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ResourceOrder"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ResourceType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Title"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Affiliate"
:description="   This table holds data related to the Affiliate records within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffCode"
      :type="String"
      :access="Edit Delete Add Read"

      :name="AffName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ContactId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="DefCommissionType"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LeadAmt"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="LeadCookieFor"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="LeadPercent"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="NotifyLead"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="NotifySale"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="ParentId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Password"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PayoutType"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="SaleAmt"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="SalePercent"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="Status"
      :type="Integer"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="CCharge"
:description="   This table holds data related to credit card charges processed from Infusionsoft through a merchant account."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Amt"
      :type="Double"
      :access="Read"

      :name="ApprCode"
      :type="String"
      :access="Read"

      :name="CCId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="MerchantId"
      :type="Id"
      :access="Read"

      :name="OrderNum"
      :type="String"
      :access="Read"

      :name="PaymentId"
      :type="Id"
      :access="Read"

      :name="RefNum"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="CProgram"
:description="   Continuity Programs"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Active"
      :type="Boolean"
      :access="Edit Add Read"

      :name="BillingType"
      :type="String"
      :access="Edit Add Read"

      :name="DefaultCycle"
      :type="String"
      :access="Edit Add Read"

      :name="DefaultFrequency"
      :type="Integer"
      :access="Edit Add Read"

      :name="DefaultPrice"
      :type="Double"
      :access="Edit Add Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="Family"
      :type="String"
      :access="Edit Add Read"

      :name="HideInStore"
      :type="Integer"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LargeImage"
      :type="Blob"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

      :name="ProgramName"
      :type="String"
      :access="Edit Add Read"

      :name="ShortDescription"
      :type="String"
      :access="Edit Add Read"

      :name="Sku"
      :type="String"
      :access="Edit Add Read"

      :name="Status"
      :type="Integer"
      :access="Edit Add Read"

      :name="Taxable"
      :type="Integer"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Campaign"
:description="   This table holds the Name and Status of Follow-up Sequences you have created within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Name"
      :type="String"
      :access="Read"

      :name="Status"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="CampaignStep"
:description="   This table holds individual follow-up sequence step data. There is one row in this table for each step found in a given follow-up sequence."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CampaignId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="StepStatus"
      :type="String"
      :access="Read"

      :name="StepTitle"
      :type="String"
      :access="Read"

      :name="TemplateId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Campaignee"
:description="   This table has one entry for each person in a single follow-up sequence. One contact in three different follow-up sequences means you will find three entries in this table for that contact record."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Campaign"
      :type="String"
      :access="Read"

      :name="CampaignId"
      :type="Id"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="Status"
      :type="Enum"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Company"
:description="   This table holds the Company data in the system."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AccountId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Address1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Street1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Street2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Street1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Street2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Anniversary"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="AssistantName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="AssistantPhone"
      :type="String"
      :access="Edit Delete Add Read"

      :name="BillingInformation"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Birthday"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="City"
      :type="String"
      :access="Edit Delete Add Read"

      :name="City2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="City3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Company"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CompanyID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="ContactNotes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ContactType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CreatedBy"
      :type="Id"
      :access="Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Email"
      :type="String"
      :access="Edit Delete Add Read"

      :name="EmailAddress2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="EmailAddress3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="FirstName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Groups"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="JobTitle"
      :type="String"
      :access="Edit Delete Add Read"

      :name="LastName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="LastUpdated"
      :type="DateTime"
      :access="Read"

      :name="LastUpdatedBy"
      :type="Id"
      :access="Read"

      :name="MiddleName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Nickname"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OwnerID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Password"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ReferralCode"
      :type="String"
      :access="Edit Delete Add Read"

      :name="SpouseName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="StreetAddress1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="StreetAddress2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Suffix"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Title"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Username"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Validated"
      :type="String"
      :access="Read"

      :name="Website"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour3"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Contact"
:description="   This table holds contact record data as well as custom contact fields. You will not see the custom fields listed in the fields below, as these are custom to each different Infusionsoft application."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AccountId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Address1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Street1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Street2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Street1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Street2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Address3Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Anniversary"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="AssistantName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="AssistantPhone"
      :type="String"
      :access="Edit Delete Add Read"

      :name="BillingInformation"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Birthday"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="City"
      :type="String"
      :access="Edit Delete Add Read"

      :name="City2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="City3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Company"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CompanyID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="ContactNotes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ContactType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Country3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CreatedBy"
      :type="Id"
      :access="Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Email"
      :type="String"
      :access="Edit Delete Add Read"

      :name="EmailAddress2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="EmailAddress3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Fax2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="FirstName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Groups"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="JobTitle"
      :type="String"
      :access="Edit Delete Add Read"

      :name="LastName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="LastUpdated"
      :type="DateTime"
      :access="Read"

      :name="LastUpdatedBy"
      :type="Id"
      :access="Read"

      :name="LeadSourceId"
      :type="Id"
      :access="Edit Add Read"

      :name="Leadsource"
      :type="String"
      :access="Edit Add Read"

      :name="MiddleName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Nickname"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OwnerID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Password"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone1Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone2Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone3Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone4Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5Ext"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Phone5Type"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="PostalCode3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ReferralCode"
      :type="String"
      :access="Edit Delete Add Read"

      :name="SpouseName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="State3"
      :type="String"
      :access="Edit Delete Add Read"

      :name="StreetAddress1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="StreetAddress2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Suffix"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Title"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Username"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Validated"
      :type="String"
      :access="Read"

      :name="Website"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour1"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour2"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ZipFour3"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ContactAction"
:description="   This table holds data for tasks, notes, and appointments within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Accepted"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="ActionDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="ActionDescription"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ActionType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CompletionDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="ContactId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="CreatedBy"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="CreationDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="CreationNotes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="EndDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="IsAppointment"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="LastUpdated"
      :type="DateTime"
      :access="Read"

      :name="LastUpdatedBy"
      :type="Id"
      :access="Read"

      :name="ObjectType"
      :type="Enum"
      :access="Edit Delete Add Read"

      :name="OpportunityId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="PopupDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Priority"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="UserID"
      :type="Id"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ContactGroup"
:description="   This table holds data for the tags you have created within Infusionsoft. In the Infusionsoft "ice age" tags were referred to as "groups", thus the table name."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="GroupCategoryId"
      :type="Id"
      :access="Edit Add Read"

      :name="GroupDescription"
      :type="String"
      :access="Edit Add Read"

      :name="GroupName"
      :type="String"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ContactGroupAssign"
:description="   This table has one entry for each tag a single contact has. If you have one contact with five tags, you will find five entries in this table for that given contact"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Contact.Address1Type"
      :type="String"
      :access="Read"

      :name="Contact.Address2Street1"
      :type="String"
      :access="Read"

      :name="Contact.Address2Street2"
      :type="String"
      :access="Read"

      :name="Contact.Address2Type"
      :type="String"
      :access="Read"

      :name="Contact.Address3Street1"
      :type="String"
      :access="Read"

      :name="Contact.Address3Street2"
      :type="String"
      :access="Read"

      :name="Contact.Address3Type"
      :type="String"
      :access="Read"

      :name="Contact.Anniversary"
      :type="Date"
      :access="Read"

      :name="Contact.AssistantName"
      :type="String"
      :access="Read"

      :name="Contact.AssistantPhone"
      :type="String"
      :access="Read"

      :name="Contact.BillingInformation"
      :type="String"
      :access="Read"

      :name="Contact.Birthday"
      :type="String"
      :access="Read"

      :name="Contact.City"
      :type="String"
      :access="Read"

      :name="Contact.City2"
      :type="String"
      :access="Read"

      :name="Contact.City3"
      :type="String"
      :access="Read"

      :name="Contact.Company"
      :type="String"
      :access="Read"

      :name="Contact.CompanyID"
      :type="Id"
      :access="Read"

      :name="Contact.ContactNotes"
      :type="String"
      :access="Read"

      :name="Contact.ContactType"
      :type="String"
      :access="Read"

      :name="Contact.Country"
      :type="String"
      :access="Read"

      :name="Contact.Country2"
      :type="String"
      :access="Read"

      :name="Contact.Country3"
      :type="String"
      :access="Read"

      :name="Contact.CreatedBy"
      :type="Id"
      :access="Read"

      :name="Contact.CustomDate1"
      :type="DateTime"
      :access="Read"

      :name="Contact.CustomDate2"
      :type="DateTime"
      :access="Read"

      :name="Contact.CustomDate3"
      :type="DateTime"
      :access="Read"

      :name="Contact.CustomDate4"
      :type="DateTime"
      :access="Read"

      :name="Contact.CustomDate5"
      :type="DateTime"
      :access="Read"

      :name="Contact.CustomDbl1"
      :type="Double"
      :access="Read"

      :name="Contact.CustomDbl2"
      :type="Double"
      :access="Read"

      :name="Contact.CustomDbl3"
      :type="Double"
      :access="Read"

      :name="Contact.CustomDbl4"
      :type="Double"
      :access="Read"

      :name="Contact.CustomDbl5"
      :type="Double"
      :access="Read"

      :name="Contact.CustomField1"
      :type="String"
      :access="Read"

      :name="Contact.CustomField10"
      :type="String"
      :access="Read"

      :name="Contact.CustomField2"
      :type="String"
      :access="Read"

      :name="Contact.CustomField3"
      :type="String"
      :access="Read"

      :name="Contact.CustomField4"
      :type="String"
      :access="Read"

      :name="Contact.CustomField5"
      :type="String"
      :access="Read"

      :name="Contact.CustomField6"
      :type="String"
      :access="Read"

      :name="Contact.CustomField7"
      :type="String"
      :access="Read"

      :name="Contact.CustomField8"
      :type="String"
      :access="Read"

      :name="Contact.CustomField9"
      :type="String"
      :access="Read"

      :name="Contact.DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Contact.Email"
      :type="String"
      :access="Read"

      :name="Contact.EmailAddress2"
      :type="String"
      :access="Read"

      :name="Contact.EmailAddress3"
      :type="String"
      :access="Read"

      :name="Contact.Fax1"
      :type="String"
      :access="Read"

      :name="Contact.Fax1Type"
      :type="String"
      :access="Read"

      :name="Contact.Fax2"
      :type="String"
      :access="Read"

      :name="Contact.Fax2Type"
      :type="String"
      :access="Read"

      :name="Contact.FirstName"
      :type="String"
      :access="Read"

      :name="Contact.Groups"
      :type="String"
      :access="Read"

      :name="Contact.HTMLSignature"
      :type="String"
      :access="Read"

      :name="Contact.Id"
      :type="Id"
      :access="Read"

      :name="Contact.JobTitle"
      :type="String"
      :access="Read"

      :name="Contact.LastName"
      :type="String"
      :access="Read"

      :name="Contact.LastUpdated"
      :type="String"
      :access="Read"

      :name="Contact.LastUpdatedBy"
      :type="String"
      :access="Read"

      :name="Contact.Leadsource"
      :type="String"
      :access="Read"

      :name="Contact.MiddleName"
      :type="String"
      :access="Read"

      :name="Contact.Nickname"
      :type="String"
      :access="Read"

      :name="Contact.OwnerID"
      :type="Id"
      :access="Read"

      :name="Contact.Phone1"
      :type="String"
      :access="Read"

      :name="Contact.Phone1Ext"
      :type="String"
      :access="Read"

      :name="Contact.Phone1Type"
      :type="String"
      :access="Read"

      :name="Contact.Phone2"
      :type="String"
      :access="Read"

      :name="Contact.Phone2Ext"
      :type="String"
      :access="Read"

      :name="Contact.Phone2Type"
      :type="String"
      :access="Read"

      :name="Contact.Phone3"
      :type="String"
      :access="Read"

      :name="Contact.Phone3Ext"
      :type="String"
      :access="Read"

      :name="Contact.Phone3Type"
      :type="String"
      :access="Read"

      :name="Contact.Phone4"
      :type="String"
      :access="Read"

      :name="Contact.Phone4Ext"
      :type="String"
      :access="Read"

      :name="Contact.Phone4Type"
      :type="String"
      :access="Read"

      :name="Contact.Phone5"
      :type="String"
      :access="Read"

      :name="Contact.Phone5Ext"
      :type="String"
      :access="Read"

      :name="Contact.Phone5Type"
      :type="String"
      :access="Read"

      :name="Contact.PostalCode"
      :type="String"
      :access="Read"

      :name="Contact.PostalCode2"
      :type="String"
      :access="Read"

      :name="Contact.PostalCode3"
      :type="String"
      :access="Read"

      :name="Contact.ReferralCode"
      :type="String"
      :access="Read"

      :name="Contact.Signature"
      :type="String"
      :access="Read"

      :name="Contact.SpouseName"
      :type="String"
      :access="Read"

      :name="Contact.State"
      :type="String"
      :access="Read"

      :name="Contact.State2"
      :type="String"
      :access="Read"

      :name="Contact.State3"
      :type="String"
      :access="Read"

      :name="Contact.StreetAddress1"
      :type="String"
      :access="Read"

      :name="Contact.StreetAddress2"
      :type="String"
      :access="Read"

      :name="Contact.Suffix"
      :type="String"
      :access="Read"

      :name="Contact.Title"
      :type="String"
      :access="Read"

      :name="Contact.Website"
      :type="String"
      :access="Read"

      :name="Contact.ZipFour1"
      :type="String"
      :access="Read"

      :name="Contact.ZipFour2"
      :type="String"
      :access="Read"

      :name="Contact.ZipFour3"
      :type="String"
      :access="Read"

      :name="ContactGroup"
      :type="String"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="GroupId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ContactGroupCategory"
:description="   This table holds tag categories. For each category you have in your system, there will be one row in this table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CategoryDescription"
      :type="String"
      :access="Edit Add Read"

      :name="CategoryName"
      :type="String"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="CreditCard"
:description="   This table holds all data tied to credit cards. For each credit card in the system there will be one row in this table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="BillAddress1"
      :type="String"
      :access="Edit Add Read"

      :name="BillAddress2"
      :type="String"
      :access="Edit Add Read"

      :name="BillCity"
      :type="String"
      :access="Edit Add Read"

      :name="BillCountry"
      :type="String"
      :access="Edit Add Read"

      :name="BillName"
      :type="String"
      :access="Edit Add Read"

      :name="BillState"
      :type="String"
      :access="Edit Add Read"

      :name="BillZip"
      :type="String"
      :access="Edit Add Read"

      :name="CVV2"
      :type="String"
      :access="Edit Add"

      :name="CardNumber"
      :type="String"
      :access="Add"

      :name="CardType"
      :type="String"
      :access="Edit Add Read"

      :name="ContactId"
      :type="Id"
      :access="Add Read"

      :name="Email"
      :type="String"
      :access="Edit Add Read"

      :name="ExpirationMonth"
      :type="String"
      :access="Edit Add Read"

      :name="ExpirationYear"
      :type="String"
      :access="Edit Add Read"

      :name="FirstName"
      :type="String"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Last4"
      :type="String"
      :access="Read"

      :name="LastName"
      :type="String"
      :access="Edit Add Read"

      :name="MaestroIssueNumber"
      :type="String"
      :access="Edit Add Read"

      :name="NameOnCard"
      :type="String"
      :access="Edit Add Read"

      :name="PhoneNumber"
      :type="String"
      :access="Edit Add Read"

      :name="ShipAddress1"
      :type="String"
      :access="Edit Add Read"

      :name="ShipAddress2"
      :type="String"
      :access="Edit Add Read"

      :name="ShipCity"
      :type="String"
      :access="Edit Add Read"

      :name="ShipCompanyName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipCountry"
      :type="String"
      :access="Edit Add Read"

      :name="ShipFirstName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipLastName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipMiddleName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipPhoneNumber"
      :type="String"
      :access="Edit Add Read"

      :name="ShipState"
      :type="String"
      :access="Edit Add Read"

      :name="ShipZip"
      :type="String"
      :access="Edit Add Read"

      :name="StartDateMonth"
      :type="String"
      :access="Edit Add Read"

      :name="StartDateYear"
      :type="String"
      :access="Edit Add Read"

      :name="Status"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="DataFormField"
:description="   This table holds custom fields. For each field there will be one row in this table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="DataType"
      :type="Integer"
      :access="Read"

      :name="DefaultValue"
      :type="String"
      :access="Edit Read"

      :name="FormId"
      :type="Id"
      :access="Read"

      :name="GroupId"
      :type="Id"
      :access="Edit Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Label"
      :type="String"
      :access="Edit Read"

      :name="ListRows"
      :type="Integer"
      :access="Edit Read"

      :name="Name"
      :type="String"
      :access="Edit Read"

      :name="Values"
      :type="String"
      :access="Edit Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="DataFormGroup"
:description="   This table holds the headers that custom fields are displayed under."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Name"
      :type="String"
      :access="Read"

      :name="TabId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="DataFormTab"
:description="   This table holds your custom field tabs. These tabs are where your custom fields sit on contact records, orders, opportunities, etc."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="FormId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="TabName"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Expense"
:description="   These are the expenses incurred by opportunities and leadsources."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="DateIncurred"
      :type="DateTime"
      :access="Read"

      :name="ExpenseAmt"
      :type="Double"
      :access="Read"

      :name="ExpenseType"
      :type="Enum"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="TypeId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="FileBox"
:description="   This table holds data related to the files stored within your company or contact fileboxes."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="Extension"
      :type="String"
      :access="Read"

      :name="FileName"
      :type="String"
      :access="Read"

      :name="FileSize"
      :type="Long"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Public"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="GroupAssign"
:description="   This table holds the data related to what user groups your system users are a part of."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Admin"
      :type="Id"
      :access="Read"

      :name="GroupId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="UserId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Invoice"
:description="   This table holds data related to an individual invoice. Remember that one order (Job) has one invoice, while one subscription (RecurringOrder) has multiple invoices."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffiliateId"
      :type="Id"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="CreditStatus"
      :type="Integer"
      :access="Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Description"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InvoiceTotal"
      :type="Double"
      :access="Read"

      :name="InvoiceType"
      :type="String"
      :access="Read"

      :name="JobId"
      :type="Id"
      :access="Read"

      :name="LeadAffiliateId"
      :type="Id"
      :access="Read"

      :name="PayPlanStatus"
      :type="Integer"
      :access="Read"

      :name="PayStatus"
      :type="Integer"
      :access="Read"

      :name="ProductSold"
      :type="String"
      :access="Read"

      :name="PromoCode"
      :type="String"
      :access="Read"

      :name="RefundStatus"
      :type="Integer"
      :access="Read"

      :name="Synced"
      :type="Integer"
      :access="Read"

      :name="TotalDue"
      :type="Double"
      :access="Read"

      :name="TotalPaid"
      :type="Double"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="InvoiceItem"
:description="   This table has one row for each "line item" found on an invoice. If there is an order for one product that also includes tax and shipping, you will find three rows on this table related to that particular InvoiceId."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CommissionStatus"
      :type="Integer"
      :access="Edit Add Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="Discount"
      :type="Double"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InvoiceAmt"
      :type="Double"
      :access="Edit Add Read"

      :name="InvoiceId"
      :type="Id"
      :access="Edit Add Read"

      :name="OrderItemId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="InvoicePayment"
:description="   This table holds one entry for each payment towards a particular invoice."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Amt"
      :type="Double"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InvoiceId"
      :type="Id"
      :access="Read"

      :name="PayDate"
      :type="Date"
      :access="Read"

      :name="PayStatus"
      :type="String"
      :access="Read"

      :name="PaymentId"
      :type="Id"
      :access="Read"

      :name="SkipCommission"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Job"
:description="   This table holds one-time order data (not subscriptions)."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="ContactId"
      :type="Id"
      :access="Edit Add Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="DueDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="JobNotes"
      :type="String"
      :access="Edit Add Read"

      :name="JobRecurringId"
      :type="Id"
      :access="Read"

      :name="JobStatus"
      :type="String"
      :access="Edit Add Read"

      :name="JobTitle"
      :type="String"
      :access="Edit Add Read"

      :name="OrderStatus"
      :type="Integer"
      :access="Edit Add Read"

      :name="OrderType"
      :type="String"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

      :name="ShipCity"
      :type="String"
      :access="Edit Add Read"

      :name="ShipCompany"
      :type="String"
      :access="Edit Add Read"

      :name="ShipCountry"
      :type="String"
      :access="Edit Add Read"

      :name="ShipFirstName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipLastName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipMiddleName"
      :type="String"
      :access="Edit Add Read"

      :name="ShipPhone"
      :type="String"
      :access="Edit Add Read"

      :name="ShipState"
      :type="String"
      :access="Edit Add Read"

      :name="ShipStreet1"
      :type="String"
      :access="Edit Add Read"

      :name="ShipStreet2"
      :type="String"
      :access="Edit Add Read"

      :name="ShipZip"
      :type="String"
      :access="Edit Add Read"

      :name="StartDate"
      :type="Date"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="JobRecurringInstance"
:description="   This table holds data related to one instance of a subscription. For each recurring of the subscription, you will find one entry in this table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AutoCharge"
      :type="Integer"
      :access="Edit Add Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="EndDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InvoiceItemId"
      :type="Id"
      :access="Edit Add Read"

      :name="RecurringId"
      :type="Id"
      :access="Edit Add Read"

      :name="StartDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Status"
      :type="Integer"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Lead"
:description="   This table holds opportunity record data."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffiliateId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="ContactID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="CreatedBy"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Edit Delete Read"

      :name="EstimatedCloseDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LastUpdated"
      :type="DateTime"
      :access="Edit Delete Read"

      :name="LastUpdatedBy"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Leadsource"
      :type="String"
      :access="Add Read"

      :name="NextActionDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="NextActionNotes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Objection"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OpportunityNotes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OpportunityTitle"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ProjectedRevenueHigh"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="ProjectedRevenueLow"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="StageID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="StatusID"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="UserID"
      :type="Id"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="LeadSource"
:description="   This table holds data related to each of the Leadsources you have created under the Setup&gt;Leadsources menu inside Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CostPerLead"
      :type="String"
      :access="Edit Add Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="EndDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LeadSourceCategoryId"
      :type="Id"
      :access="Edit Add Read"

      :name="Medium"
      :type="String"
      :access="Edit Add Read"

      :name="Message"
      :type="String"
      :access="Edit Add Read"

      :name="Name"
      :type="String"
      :access="Edit Add Read"

      :name="StartDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Status"
      :type="String"
      :access="Edit Add Read"

      :name="Vendor"
      :type="String"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="LeadSourceCategory"
:description="   Lead Source Categories"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Name"
      :type="String"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="LeadSourceExpense"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Amount"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="DateIncurred"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LeadSourceId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="LeadSourceRecurringExpenseId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Notes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Title"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="LeadSourceRecurringExpense"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Amount"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="EndDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LeadSourceId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="NextExpenseDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Notes"
      :type="String"
      :access="Edit Delete Add Read"

      :name="StartDate"
      :type="DateTime"
      :access="Edit Delete Add Read"

      :name="Title"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="MtgLead"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="ActualCloseDate"
      :type="DateTime"
      :access="Read"

      :name="ApplicationDate"
      :type="DateTime"
      :access="Read"

      :name="CreditReportDate"
      :type="DateTime"
      :access="Read"

      :name="DateAppraisalDone"
      :type="DateTime"
      :access="Read"

      :name="DateAppraisalOrdered"
      :type="DateTime"
      :access="Read"

      :name="DateAppraisalReceived"
      :type="DateTime"
      :access="Read"

      :name="DateRateLockExpires"
      :type="DateTime"
      :access="Read"

      :name="DateRateLocked"
      :type="DateTime"
      :access="Read"

      :name="DateTitleOrdered"
      :type="DateTime"
      :access="Read"

      :name="DateTitleReceived"
      :type="DateTime"
      :access="Read"

      :name="FundingDate"
      :type="DateTime"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="OrderItem"
:description="   This table holds line items for one-time orders. For each product, tax, discount, or shipping found on an order, there will be one entry in this table found."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CPU"
      :type="Double"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="ItemDescription"
      :type="String"
      :access="Edit Add Read"

      :name="ItemName"
      :type="String"
      :access="Edit Add Read"

      :name="ItemType"
      :type="Integer"
      :access="Edit Add Read"

      :name="Notes"
      :type="String"
      :access="Edit Add Read"

      :name="OrderId"
      :type="Id"
      :access="Edit Add Read"

      :name="PPU"
      :type="Double"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

      :name="Qty"
      :type="Integer"
      :access="Edit Add Read"

      :name="SubscriptionPlanId"
      :type="Id"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="PayPlan"
:description="   This table holds the PayPlan data tied to each invoice in the system."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AmtDue"
      :type="Double"
      :access="Read"

      :name="DateDue"
      :type="Date"
      :access="Read"

      :name="FirstPayAmt"
      :type="Double"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InitDate"
      :type="Date"
      :access="Read"

      :name="InvoiceId"
      :type="Id"
      :access="Read"

      :name="StartDate"
      :type="Date"
      :access="Read"

      :name="Type"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="PayPlanItem"
:description="   This table holds the data that tells our system what portion of a payment plan is due on each date."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AmtDue"
      :type="Double"
      :access="Read"

      :name="AmtPaid"
      :type="Double"
      :access="Read"

      :name="DateDue"
      :type="Date"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="PayPlanId"
      :type="Id"
      :access="Read"

      :name="Status"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Payment"
:description="   This table holds each of the payments or refunds placed. This includes all types of payments. Cash, Refund, check, PayPal, etc."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="ChargeId"
      :type="Id"
      :access="Read"

      :name="Commission"
      :type="Integer"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InvoiceId"
      :type="Id"
      :access="Read"

      :name="PayAmt"
      :type="Double"
      :access="Read"

      :name="PayDate"
      :type="Date"
      :access="Read"

      :name="PayNote"
      :type="String"
      :access="Read"

      :name="PayType"
      :type="String"
      :access="Read"

      :name="RefundId"
      :type="Id"
      :access="Read"

      :name="Synced"
      :type="Integer"
      :access="Read"

      :name="UserId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Product"
:description="   This table holds your one-time products (non subscriptions)."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="BottomHTML"
      :type="String"
      :access="Edit Add Read"

      :name="CityTaxable"
      :type="Integer"
      :access="Edit Add Read"

      :name="CountryTaxable"
      :type="Integer"
      :access="Edit Add Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="HideInStore"
      :type="Integer"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="InventoryLimit"
      :type="Integer"
      :access="Edit Add Read"

      :name="InventoryNotifiee"
      :type="String"
      :access="Edit Add Read"

      :name="IsPackage"
      :type="Integer"
      :access="Edit Add Read"

      :name="LargeImage"
      :type="Blob"
      :access="Edit Add Read"

      :name="NeedsDigitalDelivery"
      :type="Integer"
      :access="Edit Add Read"

      :name="ProductName"
      :type="String"
      :access="Edit Add Read"

      :name="ProductPrice"
      :type="Double"
      :access="Edit Add Read"

      :name="Shippable"
      :type="Integer"
      :access="Edit Add Read"

      :name="ShippingTime"
      :type="String"
      :access="Edit Add Read"

      :name="ShortDescription"
      :type="String"
      :access="Edit Add Read"

      :name="Sku"
      :type="String"
      :access="Edit Add Read"

      :name="StateTaxable"
      :type="Integer"
      :access="Edit Add Read"

      :name="Status"
      :type="Integer"
      :access="Edit Add Read"

      :name="Taxable"
      :type="Integer"
      :access="Edit Add Read"

      :name="TopHTML"
      :type="String"
      :access="Edit Add Read"

      :name="Weight"
      :type="Double"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductCategory"
:description="   This holds your products' categories and subcategories"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CategoryDisplayName"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CategoryImage"
      :type="Blob"
      :access="Edit Delete Add Read"

      :name="CategoryOrder"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="ParentId"
      :type="Id"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductCategoryAssign"
:description="   This table holds the categories that each product has been assigned to be a part of"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="ProductCategoryId"
      :type="Id"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductInterest"
:description="   This table holds data from the Product/Subscription tab on Opportunities."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="DiscountPercent"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="ObjType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="ObjectId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="ProductType"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Qty"
      :type="Integer"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductInterestBundle"
:description="   This table holds the product interest bundles that you have created from the Sales Settings section inside Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="BundleName"
      :type="String"
      :access="Edit Add Read"

      :name="Description"
      :type="String"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductOptValue"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="IsDefault"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Label"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Name"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OptionIndex"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="PriceAdjustment"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="ProductOptionId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Sku"
      :type="String"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="ProductOption"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AllowSpaces"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="CanContain"
      :type="String"
      :access="Edit Delete Add Read"

      :name="CanEndWith"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="CanStartWith"
      :type="String"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="IsRequired"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Label"
      :type="String"
      :access="Edit Delete Add Read"

      :name="MaxChars"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="MinChars"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Name"
      :type="String"
      :access="Edit Delete Add Read"

      :name="OptionType"
      :type="Enum"
      :access="Edit Delete Add Read"

      :name="Order"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="TextMessage"
      :type="Integer"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="RecurringOrder"
:description="   This table holds all the subscriptions generated on contacts. For each contact that has a subscription you will find a row in this table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffiliateId"
      :type="Id"
      :access="Edit Add Read"

      :name="AutoCharge"
      :type="Integer"
      :access="Edit Add Read"

      :name="BillingAmt"
      :type="Double"
      :access="Edit Add Read"

      :name="BillingCycle"
      :type="String"
      :access="Edit Add Read"

      :name="CC1"
      :type="Id"
      :access="Edit Add Read"

      :name="CC2"
      :type="Id"
      :access="Edit Add Read"

      :name="ContactId"
      :type="Id"
      :access="Edit Add Read"

      :name="EndDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Frequency"
      :type="Integer"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LastBillDate"
      :type="Date"
      :access="Edit Add Read"

      :name="LeadAffiliateId"
      :type="Id"
      :access="Edit Add Read"

      :name="MaxRetry"
      :type="Integer"
      :access="Edit Add Read"

      :name="MerchantAccountId"
      :type="Id"
      :access="Edit Add Read"

      :name="NextBillDate"
      :type="Date"
      :access="Read"

      :name="NumDaysBetweenRetry"
      :type="Integer"
      :access="Edit Add Read"

      :name="OriginatingOrderId"
      :type="Id"
      :access="Read"

      :name="PaidThruDate"
      :type="Date"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

      :name="ProgramId"
      :type="Id"
      :access="Edit Add Read"

      :name="PromoCode"
      :type="String"
      :access="Edit Add Read"

      :name="Qty"
      :type="Integer"
      :access="Edit Add Read"

      :name="ReasonStopped"
      :type="String"
      :access="Edit Add Read"

      :name="ShippingOptionId"
      :type="Id"
      :access="Edit Add Read"

      :name="StartDate"
      :type="Date"
      :access="Edit Add Read"

      :name="Status"
      :type="String"
      :access="Edit Add Read"

      :name="SubscriptionPlanId"
      :type="Id"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="RecurringOrderWithContact"
:description="   This is a mirror image of the RecurringOrder table, but Contact data has been virtually included here to save you an API call. Custom contact fields are not retrievable via the table."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffiliateId"
      :type="Id"
      :access="Read"

      :name="AutoCharge"
      :type="Integer"
      :access="Read"

      :name="BillingAmt"
      :type="Double"
      :access="Read"

      :name="BillingCycle"
      :type="String"
      :access="Read"

      :name="CC1"
      :type="Id"
      :access="Read"

      :name="CC2"
      :type="Id"
      :access="Read"

      :name="City"
      :type="String"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="ContactId"
      :type="Id"
      :access="Read"

      :name="Country"
      :type="String"
      :access="Read"

      :name="Email"
      :type="String"
      :access="Read"

      :name="EmailAddress2"
      :type="String"
      :access="Read"

      :name="EmailAddress3"
      :type="String"
      :access="Read"

      :name="EndDate"
      :type="Date"
      :access="Read"

      :name="FirstName"
      :type="String"
      :access="Read"

      :name="Frequency"
      :type="Integer"
      :access="Read"

      :name="HTMLSignature"
      :type="String"
      :access="Read"

      :name="LastBillDate"
      :type="Date"
      :access="Read"

      :name="LastName"
      :type="String"
      :access="Read"

      :name="LeadAffiliateId"
      :type="Id"
      :access="Read"

      :name="MaxRetry"
      :type="Integer"
      :access="Read"

      :name="MerchantAccountId"
      :type="Id"
      :access="Read"

      :name="MiddleName"
      :type="String"
      :access="Read"

      :name="NextBillDate"
      :type="Date"
      :access="Read"

      :name="Nickname"
      :type="String"
      :access="Read"

      :name="NumDaysBetweenRetry"
      :type="Integer"
      :access="Read"

      :name="PaidThruDate"
      :type="Date"
      :access="Read"

      :name="Phone1"
      :type="String"
      :access="Read"

      :name="Phone1Ext"
      :type="String"
      :access="Read"

      :name="Phone1Type"
      :type="String"
      :access="Read"

      :name="Phone2"
      :type="String"
      :access="Read"

      :name="Phone2Ext"
      :type="String"
      :access="Read"

      :name="Phone2Type"
      :type="String"
      :access="Read"

      :name="PostalCode"
      :type="String"
      :access="Read"

      :name="ProductId"
      :type="Id"
      :access="Read"

      :name="ProgramId"
      :type="Id"
      :access="Read"

      :name="PromoCode"
      :type="String"
      :access="Read"

      :name="Qty"
      :type="Integer"
      :access="Read"

      :name="ReasonStopped"
      :type="String"
      :access="Read"

      :name="RecurringOrderId"
      :type="Id"
      :access="Read"

      :name="ShippingOptionId"
      :type="Integer"
      :access="Read"

      :name="Signature"
      :type="String"
      :access="Read"

      :name="SpouseName"
      :type="String"
      :access="Read"

      :name="StartDate"
      :type="Date"
      :access="Read"

      :name="State"
      :type="String"
      :access="Read"

      :name="Status"
      :type="String"
      :access="Read"

      :name="StreetAddress1"
      :type="String"
      :access="Read"

      :name="StreetAddress2"
      :type="String"
      :access="Read"

      :name="SubscriptionPlanId"
      :type="Id"
      :access="Read"

      :name="Suffix"
      :type="String"
      :access="Read"

      :name="Title"
      :type="String"
      :access="Read"

      :name="ZipFour1"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Referral"
:description="   This table holds affiliate referrals."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="AffiliateId"
      :type="Id"
      :access="Add Read"

      :name="ContactId"
      :type="Id"
      :access="Add Read"

      :name="DateExpires"
      :type="Date"
      :access="Add Read"

      :name="DateSet"
      :type="Date"
      :access="Add Read"

      :name="IPAddress"
      :type="String"
      :access="Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Info"
      :type="String"
      :access="Add Read"

      :name="Source"
      :type="String"
      :access="Add Read"

      :name="Type"
      :type="Integer"
      :access="Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="SavedFilter"
:description="   This table holds all saved searches and saved reports created by users within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="FilterName"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="ReportStoredName"
      :type="String"
      :access="Read"

      :name="UserId"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Stage"
:description="   This table holds the opportunity stages you have created within Infusionsoft."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="StageName"
      :type="String"
      :access="Read"

      :name="StageOrder"
      :type="Integer"
      :access="Read"

      :name="TargetNumDays"
      :type="Integer"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="StageMove"
:description="   This table holds historic data of opportunities being moved from one stage to another."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CreatedBy"
      :type="Id"
      :access="Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="MoveDate"
      :type="DateTime"
      :access="Read"

      :name="MoveFromStage"
      :type="Id"
      :access="Read"

      :name="MoveToStage"
      :type="Id"
      :access="Read"

      :name="OpportunityId"
      :type="Id"
      :access="Read"

      :name="PrevStageMoveDate"
      :type="DateTime"
      :access="Read"

      :name="UserId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Status"
:description="   DEPRECATED - This table is used for 'legacy' opportunities' status field"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="StatusName"
      :type="String"
      :access="Read"

      :name="StatusOrder"
      :type="String"
      :access="Read"

      :name="TargetNumDays"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="SubscriptionPlan"
:description="   Subscription Plans"
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Active"
      :type="Boolean"
      :access="Edit Add Read"

      :name="Cycle"
      :type="String"
      :access="Edit Add Read"

      :name="Frequency"
      :type="Integer"
      :access="Edit Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="PlanPrice"
      :type="Double"
      :access="Edit Add Read"

      :name="PreAuthorizeAmount"
      :type="Double"
      :access="Edit Add Read"

      :name="ProductId"
      :type="Id"
      :access="Edit Add Read"

      :name="Prorate"
      :type="Boolean"
      :access="Edit Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Template"
:description=" "
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Categories"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="PieceTitle"
      :type="String"
      :access="Read"

      :name="PieceType"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="Ticket"
:description="   DEPRECATED - This table holds data about service tickets. This is part of a ticketing module Infusionsoft no longer offers."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CloseDate"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="ContactId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="CreatedBy"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="DateCreated"
      :type="DateTime"
      :access="Read"

      :name="DateInStage"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="DevId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="FolowUpDate"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="HasCustomerCalled"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="IssueId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="LastUpdated"
      :type="DateTime"
      :access="Read"

      :name="LastUpdatedBy"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Ordering"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="Priority"
      :type="Integer"
      :access="Edit Delete Add Read"

      :name="Stage"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="Summary"
      :type="String"
      :access="Edit Delete Add Read"

      :name="TargetCompletionDate"
      :type="Date"
      :access="Edit Delete Add Read"

      :name="TicketApplication"
      :type="String"
      :access="Edit Delete Add Read"

      :name="TicketCategory"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="TicketTitle"
      :type="String"
      :access="Edit Delete Add Read"

      :name="TicketTypeId"
      :type="Id"
      :access="Edit Delete Add Read"

      :name="TimeSpent"
      :type="Double"
      :access="Edit Delete Add Read"

      :name="UserId"
      :type="Id"
      :access="Edit Delete Add Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="TicketStage"
:description="   DEPRECATED - This table holds the ticket stages. This is part of a ticketing module Infusionsoft no longer offers."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="StageName"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="TicketType"
:description="   DEPRECATED - This table holds data related to the ticketing module Infusionsoft no longer offers."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="CategoryId"
      :type="Id"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Label"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="User"
:description="   This table holds data about your Infusionsoft users."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="City"
      :type="String"
      :access="Read"

      :name="Email"
      :type="String"
      :access="Read"

      :name="EmailAddress2"
      :type="String"
      :access="Read"

      :name="EmailAddress3"
      :type="String"
      :access="Read"

      :name="FirstName"
      :type="String"
      :access="Read"

      :name="HTMLSignature"
      :type="String"
      :access="Read"

      :name="Id"
      :type="Id"
      :access="Read"

      :name="LastName"
      :type="String"
      :access="Read"

      :name="MiddleName"
      :type="String"
      :access="Read"

      :name="Nickname"
      :type="String"
      :access="Read"

      :name="Phone1"
      :type="String"
      :access="Read"

      :name="Phone1Ext"
      :type="String"
      :access="Read"

      :name="Phone1Type"
      :type="String"
      :access="Read"

      :name="Phone2"
      :type="String"
      :access="Read"

      :name="Phone2Ext"
      :type="String"
      :access="Read"

      :name="Phone2Type"
      :type="String"
      :access="Read"

      :name="PostalCode"
      :type="String"
      :access="Read"

      :name="Signature"
      :type="String"
      :access="Read"

      :name="SpouseName"
      :type="String"
      :access="Read"

      :name="State"
      :type="String"
      :access="Read"

      :name="StreetAddress1"
      :type="String"
      :access="Read"

      :name="StreetAddress2"
      :type="String"
      :access="Read"

      :name="Suffix"
      :type="String"
      :access="Read"

      :name="Title"
      :type="String"
      :access="Read"

      :name="ZipFour1"
      :type="String"
      :access="Read"

    </tbody>

  </table>

</div>

<h3>

:table_name="UserGroup"
:description="   This table holds user group information. These are groupings for your system users, not contacts."
</p>

<thead>

      
    </thead>

    <tbody>

      :name="Id"
      :type="Id"
      :access="Read"

      :name="Name"
      :type="String"
      :access="Read"

      :name="OwnerId"
      :type="Id"
      :access="Read"

    </tbody>

  </table>

</div>

</div>
