from django.test import TestCase
from empenos.models import *


			



class Refrendo_Semanal_TestCase(TestCase):

	@classmethod
	def setUpTestData(cls):
		hoy = date.today()
		"""
			Creamos catalogos
		"""
		Sucursal.objects.create(sucursal="prueba")
		Tipo_Producto.objects.create(id = 1,tipo_producto="oro")

		User.objects.create(username="jasso208")
		Cliente.objects.create(nombre="prueba",apellido_p="prueba",estado_civil=1)
		Plazo.objects.create(id = 1,plazo="4 semanas")

		Tipo_Pago.objects.create(id = 1,tipo_pago = "Refrendo")
		Tipo_Pago.objects.create(id = 2,tipo_pago = "Comision pg")
		Estatus_Boleta.objects.create(id = 1,estatus="ABIERTA")
		Estatus_Boleta.objects.create(id = 2,estatus="CANCELADA")
		Estatus_Boleta.objects.create(id = 3,estatus="ALMONEDA")
		Estatus_Boleta.objects.create(id = 4,estatus="DESEMPEÑADA")
		Estatus_Boleta.objects.create(id = 5,estatus="REMATE")
		Estatus_Boleta.objects.create(id = 6,estatus="VENDIDA")
		Estatus_Boleta.objects.create(id = 7,estatus="APARTADA")

		Tipo_Movimiento.objects.create(id = 1,tipo_movimiento="APERTURA DE CAJA")
		Tipo_Movimiento.objects.create(id = 2,tipo_movimiento="OTROS INGRESOS")
		Tipo_Movimiento.objects.create(id = 3,tipo_movimiento="RETIRO EFECTIVO")
		Tipo_Movimiento.objects.create(id = 4,tipo_movimiento="BOLETA EMPEÑO")
		Tipo_Movimiento.objects.create(id = 5,tipo_movimiento="REFRENDO")
		Tipo_Movimiento.objects.create(id = 6,tipo_movimiento="VENTA PISO")
		Tipo_Movimiento.objects.create(id = 7,tipo_movimiento="APARTADO")
		Tipo_Movimiento.objects.create(id = 8,tipo_movimiento="ABONO APARTADO")

		Estatus_Apartado.objects.create(id = 1,estatus="apartado")
		Estatus_Apartado.objects.create(id = 2,estatus="liberado")
		Estatus_Apartado.objects.create(id = 3,estatus="vendido")
		
		"""
			TErminamos de crear catalogos
		"""
		un_dia=timedelta(days=1)

		tm = Tipo_Movimiento.objects.get(id=4)

		usuario = User.objects.get(username="jasso208")

		#creamos una boleta para la prueba		
		sucursal = Sucursal.objects.get(sucursal = "prueba")

		cie = Configuracion_Interes_Empeno()

		cie.sucursal = sucursal		
		cie.almacenaje_oro = 10
		cie.interes_oro = 20
		cie.iva_oro = 30
		cie.almacenaje_plata = 15
		cie.interes_plata = 25
		cie.iva_plata = 35
		cie.almacenaje_prod_varios = 5
		cie.interes_prod_varios = 6
		cie.iva_prod_varios = 7
		cie.usuario_modifica = usuario
		cie.save()



		tp = Tipo_Producto.objects.get(id = 1)
		caja = None
		
		avaluo = 0
		mutuo = 0
		fecha_vencimiento = datetime.combine(hoy,time.min)#para la prueba  no importa la fecha de vencimiento
		cliente = Cliente.objects.get(id=1)
		nombre_cotitular = "test_1"
		apellido_paterno = ""
		apellido_materno = ""

		plazo=Plazo.objects.get(id=1)
		fecha_vencimiento_real = fecha_vencimiento

		estatus_boleta = Estatus_Boleta.objects.get(id=7)
		estatus_apartado = Estatus_Apartado.objects.get(id=1)


		

		#la boleta con folio 1 vence hoy mismo
		boleta = Boleta_Empeno.nuevo_empeno(sucursal,tp,caja,usuario,avaluo,mutuo,fecha_vencimiento,cliente,nombre_cotitular,apellido_paterno,apellido_materno,plazo,fecha_vencimiento_real,estatus_boleta,1,tm)

		apartado=Apartado()
		apartado.folio=1
		apartado.usuario=usuario
		
		apartado.importe_venta=1000
		apartado.caja=None
		apartado.cliente=cliente
		apartado.saldo_restante=10
		apartado.estatus=estatus_apartado
		apartado.boleta=boleta
		apartado.fecha_vencimiento=fecha_vencimiento
		apartado.sucursal=sucursal
		apartado.save()

		

		#la boleta con folio 2 no venve hoy, asi que no la afecta
		boleta = Boleta_Empeno.nuevo_empeno(sucursal,tp,caja,usuario,avaluo,mutuo,fecha_vencimiento,cliente,nombre_cotitular,apellido_paterno,apellido_materno,plazo,fecha_vencimiento_real,estatus_boleta,2,tm)

		apartado=Apartado()
		apartado.folio=2
		apartado.usuario=usuario
		
		apartado.importe_venta=1000
		apartado.caja=None
		apartado.cliente=cliente
		apartado.saldo_restante=10
		apartado.estatus=estatus_apartado
		apartado.boleta=boleta
		apartado.fecha_vencimiento=fecha_vencimiento+un_dia
		apartado.sucursal=sucursal
		apartado.save()

		return True


	def test_cancela_refrendo(self):
		hoy = date.today()
		un_dia=timedelta(days = 1)
		tm = Tipo_Movimiento.objects.get(id = 4 )
		estatus_boleta = Estatus_Boleta.objects.get(id = 1)
		usuario = User.objects.get(username = "jasso208")

		#creamos una boleta para la prueba		
		sucursal = Sucursal.objects.get(sucursal = "prueba")

		tp = Tipo_Producto.objects.get(id = 1)
		caja = None
		
		avaluo = 0
		mutuo = 0
		fecha_vencimiento = datetime.combine(hoy + (timedelta(days = 14)),time.min)#para la prueba  no importa la fecha de vencimiento
		cliente = Cliente.objects.get(id=1)
		nombre_cotitular = "test_1"
		apellido_paterno = ""
		apellido_materno = ""
		plazo=Plazo.objects.get(id=1)
		fecha_vencimiento_real = fecha_vencimiento


		boleta = Boleta_Empeno.nuevo_empeno(sucursal,tp,caja,usuario,avaluo,mutuo,fecha_vencimiento,cliente,nombre_cotitular,apellido_paterno,apellido_materno,plazo,fecha_vencimiento_real,estatus_boleta,3,tm)		

		abono = Abono()
		abono.folio = 1
		abono.tipo_movimiento = Tipo_Movimiento.objects.get(id = 5)
		abono.sucursal = sucursal
		abono.fecha = (hoy - timedelta(days = 1))
		abono.usuario = usuario
		abono.importe = 100
		abono.caja = caja
		abono.boleta = boleta
		abono.save()

		#simulamos que al aplicar el abono, se generaron nuevos pagos.
		pago = Pagos()
		pago.tipo_pago = Tipo_Pago.objects.get(id = 1)
		pago.boleta = boleta
		pago.fecha_vencimiento = datetime(2021,1,1,0,0)
		pago.almacenaje = 0.00
		pago.interes = 0.00
		pago.iva = 0.00
		pago.importe = 12
		pago.vencido = "N"
		pago.pagado = "S"
		pago.fecha_pago = datetime(2021,1,1,0,0)
		pago.fecha_vencimiento_real = datetime(2021,1,1,0,0)
		pago.abono = abono
		pago.save()

		#simulamos que al aplicar el abono, se generaron nuevos pagos.
		pago2 = Pagos()
		pago2.tipo_pago = Tipo_Pago.objects.get(id = 1)
		pago2.boleta = boleta
		pago2.fecha_vencimiento = datetime(2021,1,1,0,0)
		pago2.almacenaje = 0.00
		pago2.interes = 0.00
		pago2.iva = 0.00
		pago2.importe = 12
		pago2.vencido = "N"
		pago2.pagado = "S"
		pago2.fecha_pago = datetime(2021,1,1,0,0)
		pago2.fecha_vencimiento_real = datetime(2021,1,1,0,0)
		pago2.abono = abono
		pago2.save()
		
		#simulamos que al aplicar el abono, se le otorgo un descuento.
		pago_desc = Pagos_Com_Pg_No_Usados()
		pago_desc.tipo_pago = Tipo_Pago.objects.get(id = 2)
		pago_desc.boleta = boleta
		pago_desc.fecha_vencimiento = datetime(2021,1,1,0,0)
		pago_desc.almacenaje = 0.00
		pago_desc.interes = 0.00
		pago_desc.iva = 0.00
		pago_desc.importe = 12
		pago_desc.vencido = "N"
		pago_desc.pagado = "S"
		pago_desc.fecha_pago = datetime(2021,1,1,0,0)
		pago_desc.fecha_vencimiento_real = datetime(2021,1,1,0,0)
		pago_desc.abono = abono
		pago_desc.save()


		#1.- el refrendo no puede ser cancelada si no es del dia de hoy
		resp = abono.fn_cancela_abono(usuario)

		self.assertEqual(resp[0],False)
		self.assertEqual(resp[1],"El abono no puede ser cancelado ya que no es del dia de hoy.")
		
		#2.- el refrendo no puede ser cancelada si la boleta ya presenta un refrendo posterior al que se desea cancelar.
		abono.fecha = hoy
		abono.save()


		abono2 = Abono()
		abono2.folio = 2
		abono2.tipo_movimiento = Tipo_Movimiento.objects.get(id = 5)
		abono2.sucursal = sucursal
		abono2.fecha = hoy
		abono2.usuario = usuario
		abono2.importe = 100
		abono2.caja = caja
		abono2.boleta = boleta
		abono2.save()


		resp = abono.fn_cancela_abono(usuario)
		self.assertEqual(resp[0],False)
		self.assertEqual(resp[1],"El abono no puede ser cancelado ya que existe un abono posterior al que intenta cancelar.")
		

		abono2.delete()
		#3.- La boleta a la que afecto el refrendo debe contar con el estatus anterior para poder regresar el estatus.
		resp = abono.fn_cancela_abono(usuario)
		self.assertEqual(resp[0],False)
		self.assertEqual(resp[1],"El abono no puede ser cancelado ya que no es posible calcular el estatus de boleta anterior.")

		boleta.estatus_anterior = Estatus_Boleta.objects.get(id = 3)
		boleta.save()
		#4.- La boleta a la que afecto el refrendo debe contar con la fecha de vencimiento anteriory la fecha de vencimiento real anterior.


		resp = abono.fn_cancela_abono(usuario)

		self.assertEqual(resp[0],False)
		self.assertEqual(resp[1],"El abono no puede ser cancelado ya que no es posible calcular la fecha de vencimiento anterior.")

		

		boleta.fecha_vencimiento_anterior = datetime.combine(hoy,time.min)
		boleta.save()

		#4.- La boleta a la que afecto el refrendo debe contar con  la fecha de vencimiento real anterior.
	
		resp = abono.fn_cancela_abono(usuario)	


		self.assertEqual(resp[0],False)
		self.assertEqual(resp[1],"El abono no puede ser cancelado ya que no es posible calcular la fecha de vencimiento anterior.")
		

		boleta.fecha_vencimiento_real_anterior = datetime.combine(hoy - timedelta(days = 1),time.min)
		boleta.save()
		
		resp = abono.fn_cancela_abono(usuario)		

		#5.- Si al refrendo se le aplicaron descuentos, se restauran los descuentos	

		pagos_desc = Pagos_Com_Pg_No_Usados.objects.filter(abono = abono)	
		comision_pg = Pagos.objects.filter(boleta = boleta,tipo_pago__id = 2)
		self.assertEqual(pagos_desc.exists(),False)
		self.assertEqual(comision_pg.exists(),True)

		#.- Si el refrendo saldo comision de periodo de gracia, las marca como no pagadas.
		#.- Si el refrendo aplico abono a capital, agreamos el abono a capital al mutuo 		
		#.- Regresamos la boleta a su estatus original.
		self.assertEqual(boleta.estatus,Estatus_Boleta.objects.get(id = 3))
		#.- Regresamos la fecha de vencimiento de la boleta a su fecha original.
		self.assertEqual(boleta.fecha_vencimiento,datetime.combine(hoy,time.min))
		self.assertEqual(boleta.fecha_vencimiento_real,datetime.combine((hoy - timedelta(days = 1)),time.min))

		#.- Si al apliar el refrendo se generaron nuevos pagos, los eliminamos
		#pagos = Pagos.objects.filter(abono = abono)
		#no necesitamos validar esto, ya que el abono se elimino 
		abono = Abono.objects.get(id = 1)
		self.assertEqual(int(abono.importe),0)
		self.assertEqual(abono.estatus,"CANCELADO")
		
		
		
		



