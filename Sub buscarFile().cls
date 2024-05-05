Sub buscarFile()
    Dim ws As Worksheet
    Dim fd As FileDialog
    Dim items As FileDialogSelectedItems
    Dim ruta As String
    Set fd = Application.FileDialog(msoFileDialogFilePicker)
    Set ws = ThisWorkbook.Sheets(1)
    With fd
    .Title = "Obtener la ruta del archivo"
    .AllowMultiSelect = False
    .Filters.Add "Archivos excel", "*.xls, *.xlsx, *.xlsm"
    .Show
    End With
    
    Set items = fd.SelectedItems
    If items.Count > 0 Then
    rutas = items(1)
    ws.Range("C2").Value = rutas
    End If
    End Sub
    
    Sub renameSheets()
        Dim ws As Worksheet
        Dim fd As FileDialog
        Dim items As FileDialogSelectedItems
        Dim ruta As String
        Dim workbookToOpen As Workbook
        Dim dataRange As Range
        Dim i As Integer
    
        ' Referencia a la hoja donde está el botón
        Set ws = ThisWorkbook.Sheets(1)
    
        ' Obtener la ruta del archivo
        ruta = ws.Range("C2").Value
    
        If ruta = "" Then
            MsgBox "Primero selecciona un archivo utilizando la función buscarFile()"
            Exit Sub
        End If
    
        ' Abrir el libro
        Set workbookToOpen = Workbooks.Open(ruta)
    
        ' Definir la hoja activa del libro abierto
        Set ws = workbookToOpen.Sheets(1)
    
        ' Obtener el rango de datos
        Set dataRange = ws.Range("C9:E9").Resize(ws.Cells(ws.Rows.Count, "C").End(xlUp).Row - 8)
    
        ' Renombrar las hojas del libro abierto
        For i = 1 To workbookToOpen.Sheets.Count
            workbookToOpen.Sheets(i).Name = dataRange.Cells(i, 1).Value
        Next i
    
        ' Cerrar el libro sin guardar cambios
        workbookToOpen.Close False
    End Sub
    