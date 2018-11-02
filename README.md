# skyblue-django


### Trigger CASCADE !

CREATE TRIGGER [delete_doc]
BEFORE DELETE
ON [app_skyblue_condominio]
FOR EACH ROW
BEGIN
DELETE FROM app_skyblue_documentoinstitucional WHERE condominio_id = old.id;
END
