<#
.SYNOPSIS
    IdentityOS sample Microsoft Graph action script.

.DESCRIPTION
    This script provides lab-safe sample Microsoft Graph PowerShell actions
    that demonstrate how IdentityOS lifecycle, access, governance, and audit
    decisions could map to Microsoft Entra ID actions.

    This script is designed for documentation and lab demonstration only.

    By default, the script runs in dry-run mode and does not execute changes.

.NOTES
    Project: IdentityOS
    Phase: v0.7.0 - Microsoft Entra ID Integration Blueprint
    Author: Renard Priester
#>

param(
    [switch]$Execute
)

$DryRun = -not $Execute

$RequiredScopes = @(
    "User.ReadWrite.All",
    "Group.ReadWrite.All",
    "GroupMember.ReadWrite.All",
    "Application.Read.All",
    "AppRoleAssignment.ReadWrite.All",
    "Directory.Read.All",
    "AuditLog.Read.All"
)

function Write-IdentityOSBanner {
    Write-Host ""
    Write-Host "====================================================="
    Write-Host " IdentityOS - Sample Microsoft Graph Actions"
    Write-Host "====================================================="
    Write-Host ""
    Write-Host "Mode: $(if ($DryRun) { 'DRY RUN - no changes will be made' } else { 'EXECUTE - changes may be made' })"
    Write-Host ""
}

function Write-IdentityOSAction {
    param(
        [string]$Action,
        [string]$Details
    )

    Write-Host "[IdentityOS Action] $Action"
    Write-Host "  $Details"
    Write-Host ""
}

function Connect-IdentityOSGraph {
    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Graph Connection Skipped" `
            -Details "Dry-run mode enabled. Would connect with scopes: $($RequiredScopes -join ', ')"

        return
    }

    Connect-MgGraph -Scopes $RequiredScopes
}

function New-IdentityOSJoinerUser {
    param(
        [string]$DisplayName,
        [string]$UserPrincipalName,
        [string]$MailNickname,
        [string]$Department,
        [string]$JobTitle,
        [string]$UsageLocation = "US"
    )

    $TemporaryPassword = "ChangeMe-IdentityOS-123!"

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Create Joiner User" `
            -Details "Would create user $DisplayName <$UserPrincipalName> in department $Department with title $JobTitle."

        return
    }

    New-MgUser `
        -DisplayName $DisplayName `
        -UserPrincipalName $UserPrincipalName `
        -MailNickname $MailNickname `
        -Department $Department `
        -JobTitle $JobTitle `
        -UsageLocation $UsageLocation `
        -AccountEnabled `
        -PasswordProfile @{
            Password = $TemporaryPassword
            ForceChangePasswordNextSignIn = $true
        }
}

function Update-IdentityOSMoverUser {
    param(
        [string]$UserId,
        [string]$NewDepartment,
        [string]$NewJobTitle
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Update Mover User" `
            -Details "Would update user $UserId to department $NewDepartment and title $NewJobTitle."

        return
    }

    Update-MgUser `
        -UserId $UserId `
        -Department $NewDepartment `
        -JobTitle $NewJobTitle
}

function Disable-IdentityOSLeaverUser {
    param(
        [string]$UserId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Disable Leaver User" `
            -Details "Would disable user account $UserId."

        return
    }

    Update-MgUser `
        -UserId $UserId `
        -AccountEnabled:$false
}

function Revoke-IdentityOSUserSessions {
    param(
        [string]$UserId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Revoke User Sessions" `
            -Details "Would revoke sign-in sessions for user $UserId."

        return
    }

    Revoke-MgUserSignInSession -UserId $UserId
}

function Add-IdentityOSGroupMember {
    param(
        [string]$GroupId,
        [string]$DirectoryObjectId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Add Group Member" `
            -Details "Would add directory object $DirectoryObjectId to group $GroupId."

        return
    }

    New-MgGroupMemberByRef `
        -GroupId $GroupId `
        -OdataId "https://graph.microsoft.com/v1.0/directoryObjects/$DirectoryObjectId"
}

function Remove-IdentityOSGroupMember {
    param(
        [string]$GroupId,
        [string]$DirectoryObjectId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Remove Group Member" `
            -Details "Would remove directory object $DirectoryObjectId from group $GroupId."

        return
    }

    Remove-MgGroupMemberByRef `
        -GroupId $GroupId `
        -DirectoryObjectId $DirectoryObjectId
}

function Add-IdentityOSAppRoleAssignment {
    param(
        [string]$UserId,
        [string]$PrincipalId,
        [string]$ResourceId,
        [string]$AppRoleId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Add App Role Assignment" `
            -Details "Would assign app role $AppRoleId on resource $ResourceId to principal $PrincipalId."

        return
    }

    $Body = @{
        principalId = $PrincipalId
        resourceId  = $ResourceId
        appRoleId   = $AppRoleId
    }

    Invoke-MgGraphRequest `
        -Method POST `
        -Uri "https://graph.microsoft.com/v1.0/users/$UserId/appRoleAssignments" `
        -Body ($Body | ConvertTo-Json -Depth 5) `
        -ContentType "application/json"
}

function Remove-IdentityOSAppRoleAssignment {
    param(
        [string]$UserId,
        [string]$AppRoleAssignmentId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Remove App Role Assignment" `
            -Details "Would remove app role assignment $AppRoleAssignmentId from user $UserId."

        return
    }

    Invoke-MgGraphRequest `
        -Method DELETE `
        -Uri "https://graph.microsoft.com/v1.0/users/$UserId/appRoleAssignments/$AppRoleAssignmentId"
}

function Get-IdentityOSUserAccessSnapshot {
    param(
        [string]$UserId
    )

    if ($DryRun) {
        Write-IdentityOSAction `
            -Action "Access Snapshot" `
            -Details "Would collect user profile, group memberships, app role assignments, and audit evidence for user $UserId."

        return
    }

    $User = Get-MgUser -UserId $UserId
    $Groups = Get-MgUserMemberOf -UserId $UserId
    $AppRoles = Invoke-MgGraphRequest `
        -Method GET `
        -Uri "https://graph.microsoft.com/v1.0/users/$UserId/appRoleAssignments"

    [PSCustomObject]@{
        User = $User
        Groups = $Groups
        AppRoleAssignments = $AppRoles
    }
}

function Invoke-IdentityOSJoinerExample {
    Write-IdentityOSAction `
        -Action "Joiner Example" `
        -Details "Demonstrates user creation and baseline group assignment."

    New-IdentityOSJoinerUser `
        -DisplayName "Morgan Lee" `
        -UserPrincipalName "morgan.lee@contoso.example" `
        -MailNickname "morgan.lee" `
        -Department "Finance" `
        -JobTitle "Financial Analyst"

    Add-IdentityOSGroupMember `
        -GroupId "00000000-0000-0000-0000-000000000001" `
        -DirectoryObjectId "00000000-0000-0000-0000-000000000101"
}

function Invoke-IdentityOSMoverExample {
    Write-IdentityOSAction `
        -Action "Mover Example" `
        -Details "Demonstrates attribute update, old access removal, and new access assignment."

    Update-IdentityOSMoverUser `
        -UserId "00000000-0000-0000-0000-000000000201" `
        -NewDepartment "Legal" `
        -NewJobTitle "Legal Operations Analyst"

    Remove-IdentityOSGroupMember `
        -GroupId "00000000-0000-0000-0000-000000000301" `
        -DirectoryObjectId "00000000-0000-0000-0000-000000000201"

    Add-IdentityOSGroupMember `
        -GroupId "00000000-0000-0000-0000-000000000302" `
        -DirectoryObjectId "00000000-0000-0000-0000-000000000201"
}

function Invoke-IdentityOSLeaverExample {
    Write-IdentityOSAction `
        -Action "Leaver Example" `
        -Details "Demonstrates access snapshot, account disablement, session revocation, and access removal."

    Get-IdentityOSUserAccessSnapshot `
        -UserId "00000000-0000-0000-0000-000000000401"

    Disable-IdentityOSLeaverUser `
        -UserId "00000000-0000-0000-0000-000000000401"

    Revoke-IdentityOSUserSessions `
        -UserId "00000000-0000-0000-0000-000000000401"

    Remove-IdentityOSGroupMember `
        -GroupId "00000000-0000-0000-0000-000000000501" `
        -DirectoryObjectId "00000000-0000-0000-0000-000000000401"
}

function Invoke-IdentityOSAuditEvidenceExample {
    Write-IdentityOSAction `
        -Action "Audit Evidence Example" `
        -Details "Would collect evidence from user profile, group memberships, app assignments, and directory audit logs."

    Get-IdentityOSUserAccessSnapshot `
        -UserId "00000000-0000-0000-0000-000000000601"
}

Write-IdentityOSBanner

Write-Host "This script is a sample reference for IdentityOS Microsoft Graph actions."
Write-Host "It is safe by default because it runs in dry-run mode unless -Execute is used."
Write-Host ""

Connect-IdentityOSGraph

Write-Host "Available sample functions:"
Write-Host "  Invoke-IdentityOSJoinerExample"
Write-Host "  Invoke-IdentityOSMoverExample"
Write-Host "  Invoke-IdentityOSLeaverExample"
Write-Host "  Invoke-IdentityOSAuditEvidenceExample"
Write-Host ""
Write-Host "Example dry-run command:"
Write-Host "  .\sample-graph-actions.ps1"
Write-Host ""
Write-Host "Example execute command for lab tenant only:"
Write-Host "  .\sample-graph-actions.ps1 -Execute"
Write-Host ""
Write-Host "WARNING: Do not use -Execute in production. Test only in a lab tenant."