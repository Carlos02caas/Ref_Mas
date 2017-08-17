from django import forms

from mascota.models import Mascota

class MascotaForm(forms.ModelForm):
	class Meta:
		model=Mascota

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rexcate',
			'persona',
			'vacuna',
		]
		labels ={
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad Aproximada' ,
			'fecha_rexcate': 'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
		widgets ={
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rexcate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}