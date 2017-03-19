from django.conf.urls import patterns, url

from transporte import views

urlpatterns = [
	url(r'^login' , 'django.contrib.auth.views.login',
		{'template_name':'login.html'}, name='login'),
	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),

	url(r'^inicio/', views.InicioView, name='inicio'),
	url(r'^rutas/', views.RutasView, name='rutas'),
	url(r'^ubicacion/', views.UbicacionView, name='ubicacion'),
	url(r'^troncales/', views.RutaTView, name='troncales'),
	url(r'^norte/', views.RutaNorteView, name='norte'),
	url(r'^sur/', views.RutaSurView, name='sur'),
	url(r'^centro/', views.RutaCentroView, name='centro'),
	url(r'^este/', views.RutaEsteView, name='este'),
	url(r'^noroeste/', views.RutaNOesteView, name='noroeste'),
	url(r'^suroeste/', views.RutaSOesteView, name='suroeste'),
	url(r'^Troncal1/', views.UbT1View, name='Troncal1'),
	url(r'^Troncal2/', views.UbT2View, name='Troncal2'),
	url(r'^Troncal3/', views.UbT1View, name='Troncal3'),
	url(r'^R-25Julio-Pradera/', views.R25JPView, name='Ruta-Alimentadora-25-de-Julio-Pradera'),
	url(r'^R-alborada/', views.RalboradaView, name='Ruta-Alimentadora-Alborada'),
	url(r'^R-causarina/', views.RcausarinaView, name='Ruta-Alimentadora-Casuarina'),
	url(r'^R-centro/', views.RcentroView, name='Ruta-Alimentadora-Centro'),
	url(r'^R-estelaMaris-Pradera/', views.RestelaView, name='Ruta-Alimentadora-EstelaMaris-Padera'),
	url(r'^R-fertisa/', views.RfertisaView, name='Ruta-Alimentadora-Fertisa'),
	url(r'^R-flor-de-bastion/', views.RflorbastionView, name='Ruta-Alimentadora-Flor-de-Bastion'),
	url(r'^R-floresta/', views.RflorestaView, name='Ruta-Alimentadora-Floresta'),
	url(r'^R-florida-rotonda/', views.RfloridarotView, name='Ruta-Alimentadora-Florida-Rotonda'),
	url(r'^R-garzota/', views.RgarzotaView, name='Ruta-Alimentadora-Garzota'),
	url(r'^R-GuasmoCentral/', views.RguasmocentralView, name='Ruta-Alimentadora-GuasmoCentral'),
	url(r'^R-GuasmoSur-Cristal/', views.RguasmosurcristalView, name='Ruta-Alimentadora-GuasmoSur-Cristal'),
	url(r'^R-guayacanes/', views.RguayacanesView, name='Ruta-Alimentadora-Guayacanes'),
	url(r'^R-iguanas/', views.RiguanasView, name='Ruta-Alimentadora-Iguanas'),	
	url(r'^R-juan-montalvo/', views.RjuanmontalvoView, name='Ruta-Alimentadora-JuanMontalvo'),
	url(r'^R-juan-tancamarengo/', views.RjuantancaView, name='Ruta-Alimentadora-JuanTancaMarengo'),
	url(r'^R-laPlayita/', views.RlaPlayitaView, name='Ruta-Alimentadora-LaPlayita'),
	url(r'^R-mapasingue-este/', views.RmapasingueEView, name='Ruta-Alimentadora-Mapasingue-Este'),	
	url(r'^R-mapasingue-oeste/', views.RmapasingueOView, name='Ruta-Alimentadora-Mapasingue-Oeste'),
	url(r'^R-mucholote-O/', views.RmucholoteOView, name='Ruta-Alimentadora-MuchoLote-O'),
	url(r'^R-mucholote-G/', views.RmucholoteGView, name='Ruta-Alimentadora-MuchoLote-G'),
	url(r'^R-orellana/', views.RorellanaView, name='Ruta-Alimentadora-Orellana'),
	url(r'^R-pascuales/', views.RpascualesView, name='Ruta-Alimentadora-Pascuales'),
	url(r'^R-puertomaritimo/', views.RpuertoView, name='Ruta-Alimentadora-PuertoMaritimo'),
	url(r'^R-samanes/', views.RsamanesView, name='Ruta-Alimentadora-Samanes'),
	url(r'^R-suces/', views.RsaucesView, name='Ruta-Alimentadora-Sauces'),
	url(r'^R-trinipuerto/', views.RtrinipuertoView, name='Ruta-Alimentadora-Trinipuerto'),
	url(r'^R-trinitaria-2dopuente/', views.Rtrinitaria2View, name='Ruta-Alimentadora-Trinitaria-2Puente'),
	url(r'^R-UdeBastion/', views.RUBastionView, name='Ruta-Alimentadora-U-de-Bastion'),
	url(r'^R-VialaCosta/', views.RVialaCostaView, name='Ruta-Alimentadora-Via-la-Costa'),
	url(r'^R-atahualpa-sanAgustin/', views.RatahualpaSAView, name='Ruta-Alimentadora-atahualpa-SanAgustin'),
	url(r'^R-losEsteros/', views.RlosEsterosView, name='Ruta-Alimentadora-losEsteros'),
	url(r'^R-martinAviles/', views.RmartinAvilesView, name='Ruta-Alimentadora-martinAviles'),
	url(r'^R-playita-sanAgustin/', views.RplayitaSAView, name='Ruta-Alimentadora-playita-sanAgustin'),
	url(r'^miRuta/', views.MiRutaView, name='Mi-Ruta'),
	url(r'^admin/', views.AdminView, name='admin'),
	url(r'^agregarVehiculo/', views.Create_VehiculoView, name='agregarVehiculos'),
	url(r'^editarVehiculo/', views.EditarView, name='editarVehiculos'),
	url(r'^velocimetro/', views.VelocimetroView, name='velocimetro'),
	url(r'^paradas/', views.ParadasView, name='paradas'),
	url(r'^agregarconductores/', views.Create_conductoresView, name='agregarConductores'),
	url(r'^rutavehiculo/', views.Create_Ruta_VehiculoView, name='createrutavehiculo'),
	url(r'^rutavehiculo/', views.listarutavehiculo, name='rutavehiculolist'),
	url(r'^informacionVehiculo/', views.listavehiculo, name='informacionvehiculo'),
	url(r'^informacionConductores/', views.listaconductores, name='informacionconductores'),

	url(r'^mapa/', views.trazarMapa, name='mapa'),
	url(r'^conection/', views.create_posCar, name='conection'),
	url(r'^lcar/(?P<id_v>\w+)/', views.get_pos_car, name='get_pos_car'),  # JSON lat, vel, long
	url(r'^lruta/(?P<id_lr>\w+)/', views.get_rline, name='get_lruta'),  # JSON lat, long
	url(r'^lparada/(?P<id_p_ruta>\w+)/', views.get_pos_parada, name='get_lparada'),  # JSON lat, vel,
	url(r'^lista/(?P<id_p_ruta>\w+)/', views.get_lista, name='get_lista'),  # JSON lat, vel, long
	url(r'^listapar/(?P<id_p_ruta>\w+)/', views.get_pline, name='get_lista_parada'),  # JSON lat, vel, long
]
