---
password: INJECT_ADMIN_PASSWORD
---

## Housekeeping

The **Housekeeping** feature in iTextPRO offers a powerful tool to **reset Master Billing Data** in a single action. This option is intended for administrative use in situations where a fresh setup or cleanup of billing data is required.

!!! danger "Important"
    Once deleted, data **cannot be restored**. Use this feature with extreme caution.

---

### ️ How to Use Housekeeping

1. Navigate to the **Housekeeping** section.
2. You will see a list of **Master Billing Data tables** with toggle switches labeled **Yes/No** next to each.
3. To reset data from a specific table, switch the toggle to **Yes**.
4. After selecting the necessary tables, click the **Reset** button.

---

### ️ Master Data Alert

Upon clicking the Reset button:

- iTextPRO displays a **Master Data Alert** popup.
- You will be prompted with an option to **take a backup** of your data before proceeding.
- After confirmation, iTextPRO will **permanently delete** the selected billing data.

!!! warning "Backup Recommended"
    It is **strongly recommended** to back up your data before using this feature.

---

### When to Use Housekeeping

- When setting up a **fresh billing environment**.
- During major **data cleanup** or **test data removal**.
- After performing **system migrations** or **environment resets**.

---

Housekeeping is a **rarely used but critical** feature in iTextPRO for system maintenance and data hygiene. Always proceed carefully and ensure that you have appropriate backups in place before executing a reset.
