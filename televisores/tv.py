class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV._numTV += 1

    #Metodos set

    def setMarca(self, marca):
        self._marca = marca
    
    def setControl(self, control):
        self._control = control
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def setVolumen(self, volumen):
        if (volumen < 0 or volumen > 7) and self._estado == False:
            return
        self._volumen = volumen
    
    def setCanal(self, canal):
        if (canal < 1 or canal > 120) and self._estado == False:
            return
        self._canal = canal

    #Metodos get

    def getMarca(self):
        return self._marca
    
    def getControl(self):
        return self._control
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getCanal(self):
        return self._canal

    def getEstado(self):
        return self._estado

    #Metodos set y get de clase

    @classmethod
    def setNumTV(cls, numTV):
        TV._numTV = numTV

    @classmethod
    def getNumTV(cls, numTV):
        TV._numTV = numTV

    #Metodos

    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if self._canal == 120 and self._estado == False:
            return
        self._canal += 1
    
    def canalDown(self):
        if self._canal == 1 and self._estado == False:
            return
        self._canal -= 1
    
    def volumenUp(self):
        if self._volumen == 7 and self._estado == False:
            return
        self._volumen += 1
    
    def volumenUp(self):
        if self._volumen == 0 and self._estado == False:
            return
        self._volumen -= 1