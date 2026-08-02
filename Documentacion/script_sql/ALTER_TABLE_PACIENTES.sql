-- Ubicacion_Documento
ALTER TABLE Paciente
DROP CONSTRAINT IF EXISTS uq_ubicacion_documento,
ADD COLUMN Ubicacion_Documento VARCHAR(500),
ADD CONSTRAINT uq_ubicacion_documento UNIQUE(Ubicacion_Documento);