import frappe

def after_migrate():
    system_settings = frappe.get_doc('System Settings', 'System Settings')
    system_settings.db_set('disable_standard_email_footer', 1)
    system_settings.db_set('hide_footer_in_auto_email_reports', 1)
    system_settings.db_set('email_footer_address', "Sent Via Velobiotics")

    translations = [
        ["ERPNext Integrations", "Velobiotics Integrations"],
        ["ERPNext Settings", "Velobiotics Settings"],
        ["ERPNext", "Velobiotics"]
    ]
    
    for row in translations:
        if not frappe.db.exists("Translation", {"source_text": row[0], "translated_text": row[1]}):
            frappe.get_doc({
                "doctype": "Translation",
                "source_text": row[0],
                "translated_text": row[1]
            }).save()