from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse

class Estatus(models.Model):	
	estatus=models.CharField(max_length=20)
	
	def __str__(self):
		return str(self.id)+' '+self.estatus
		
class Proveedor(models.Model):
	proveedor=models.CharField(max_length=40,null=False)
	id_estatus=models.ForeignKey(Estatus,on_delete=models.PROTECT,default=1)
	
	def __str__(self):
		return self.proveedor
		
class Productos(models.Model):	
	nombre=models.CharField(max_length=100)
	desc_producto=models.TextField()
	precio=models.DecimalField(max_digits=26,decimal_places=2,default=0.00)
	descuento=models.IntegerField(default=0)	
	id_proveedor=models.ForeignKey(Proveedor,on_delete=models.PROTECT,null=True)
	marca=models.CharField(max_length=100,null=False,default="")
	clave_prod_proveedor=models.CharField(max_length=20,null=True)
	id_estatus=models.ForeignKey(Estatus,on_delete=models.PROTECT,default=1)
	precio_proveedor=models.DecimalField(max_digits=26,decimal_places=2,default=0.00,null=False)
	

	def __str__(self):
		return str(self.id)+' '+self.nombre
	
	def get_absolute_url(self):
		return reverse('edicion_producto', kwargs={'id_producto': self.id})
		
class Atributos(models.Model):
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
	atributo=models.CharField(max_length=50)
	valor_atributo=models.CharField(max_length=50)
	
	def __str__(self):
		return self.atributo
		
	class Meta:
		unique_together=('id_producto','atributo')
	
class Tallas(models.Model):
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
	talla=models.CharField(max_length=10)
	entrada=models.IntegerField(default=0)
	salida=models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.id_producto.id)+' '+self.id_producto.nombre+' '+self.talla
	
	class Meta:
		unique_together=('id_producto','talla')
		
class Img_Producto(models.Model):
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
	nom_img=models.CharField(max_length=7)
	orden=models.IntegerField()
	
	def __str__(self):
		return self.nom_img
	class Meta:
		unique_together=('id_producto','orden')

class Productos_Relacionados(models.Model):
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT,related_name='producto')
	id_producto_relacionado=models.ForeignKey(Productos,on_delete=models.PROTECT,related_name='prod_relacionado')
	
	def __str__(self):
		return self.id_producto.nombre+'=>'+self.id_producto_relacionado.nombre
		
	class Meta:
		unique_together=('id_producto','id_producto_relacionado')

class Municipio(models.Model):
	municipio=models.CharField(max_length=50,null=False)
	
class Estado(models.Model):
	estado=models.CharField(max_length=50,null=False)
	
class Pais(models.Model):
	pais=models.CharField(max_length=50,null=False)
	

	
class Categorias(models.Model):
	categoria=models.CharField(max_length=50,null=False)
	
	def __str__(self):
		return str(self.id)+' '+self.categoria
	
	class Meta:
		unique_together=("categoria",)
class Rel_Producto_Categoria(models.Model):
	id_producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
	id_categoria=models.ForeignKey(Categorias,on_delete=models.PROTECT)
	
	def __str__(self):
		return "["+str(self.id_categoria.id)+' '+self.id_categoria.categoria+'] '+self.id_producto.nombre
		
	class Meta:
		unique_together=("id_producto","id_categoria",)
		
