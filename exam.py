
import httplib, urllib

class MacChange(object):
	"""docstring for MacChange"""
	def __init__(self, url):
		super(MacChange, self).__init__()
		self.cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
		self.conexion = httplib.HTTPConnection(url)
		self.login()
		self.html = "empty"
		self.i = 1

	def login(self):
		parametros = urllib.urlencode({'username': 'admin','password':'cachiflin'})
		self.conexion.request("POST", "/login.ccp", parametros, self.cabeceras)
		respuesta = self.conexion.getresponse()
		self.html = respuesta.read()
		return respuesta.status

	def addMac(self, name, mac):
		parametros = urllib.urlencode({
			'ccp_act' : 'set',
			'ccpSubEvent' : 'CCP_SUB_MACFILTER',
			'nextPage' : 'filters.htm',
			'macList_Name_1.1.'+str(self.i)+'.0.0' : name,
			'macList_MACAddress_1.1.'+str(self.i)+'.0.0' : mac,
			})
		self.conexion.request("POST", "/get_set.ccp", parametros, self.cabeceras)
		respuesta = self.conexion.getresponse()
		self.html = respuesta.read()
		self.i += 1
		return respuesta.status

	def __del__(self):
		self.conexion.close()

def main():
	datos = {
		"Arturo PC":"40:16:7E:22:4E:43",
		"Ricardo PC":"00:08:CA:6E:65:72",
		"IESFROSUR-PC":"5C:AC:4C:B0:AD:89",
		"JOLGUER PC":"48:5A:B6:BA:EF:4F",
		"AHM PC":"00:08:CA:6E:65:72",
		#cel
		"Arturo Cel":"88:32:9B:AB:9D:A3",
		"Ricardo Cel":"40:0E:85:2D:39:17",
		"Jolguer Cel":"E4:2D:02:E9:D8:7C",
		"AHM Cel":"60:BE:B5:8E:BB:60",
	}

	cam = {
		"Abraham PC":"3C:77:E6:54:E9:37",
		"Secretaria del cam":"00:22:5F:6D:49:26",
		"COELLO PC":"74:DE:2B:84:87:B6",
		"CLAUDIA-HP":"64:27:37:01:9B:89",
		"Tio Rica PC":"E0:B9:A5:19:32:4C",
	}

	#Alex 90:00:4E:AE:1A:9B

	change = MacChange("192.168.1.67:8080")
	for name, mac in cam.iteritems():
		print change.addMac(name, mac)

if __name__ == '__main__':
	main()
