from behave import *

@then('Go to the "Change Password" page https://devcloud.connectedio.com/profile/change-password')
def go_to_chng_pswrd_pg(context):
    """
    Hover over the Logout button at the right corner of the Header and click on the button Logout
    """
    context.app.main_page.go_to_chng_pswrd_pg()


@then('Enter the old password in the field "New Password" {old_pswd}')
def ntr_old_pswd(context, old_pswd):
    """
    Enter the old password in the field "New Password" manicpiano731
    """
    context.app.main_page.ntr_old_pswd(old_pswd)


@step('Enter the old password in the field "Confirm New Password" {old_pswd}')
def cfrm_old_pswd(context, old_pswd):
    """
    Enter the old password in the field "Confirm New Password" manicpiano731
    """
    context.app.main_page.cfrm_old_pswd(old_pswd)


@then('Click on the button "Save"')
def clck_on_btn_save(context):
    """
    Click on the button "Save"
    """
    context.app.main_page.clck_on_btn_save()


@step("Verify the message is displayed: Old and new password cannot be same.")
def clck_on_btn_save(context):
    """
    Verify the message is displayed: Old and new password cannot be same.
    """
    context.app.main_page.clck_on_btn_save()