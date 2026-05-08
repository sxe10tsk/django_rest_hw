from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500)

	def __str__(self):
		return self.name


class Measurement(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
	temperature = models.DecimalField(max_digits=3, decimal_places=1, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	sensor_image = models.ImageField(
		max_length=None,
		blank=True,
		upload_to='measurement/',
		null=True
	)

	def __str__(self):
		return f'Температура {self.temperature}°C в {self.sensor.name}'



