    for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                item = QtWidgets.QTableWidgetItem(str(dato))
                self.tableWidget.setItem(fila, columna, item)