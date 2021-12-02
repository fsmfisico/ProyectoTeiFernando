float valo; 
float val = 0;
int state = 0; // 0 LED apagado, mientras que 1 encendido
int old_val = 0;
float entrada = 0;
const int BOTON = 7;
void setup(){
Serial.begin(9600);
pinMode(BOTON,INPUT); // y BOTON como señal de entrada
}

void loop(){
val= digitalRead(BOTON); // lee el estado del Boton

if ((val == HIGH) && (old_val == LOW)){
state=1-state;

}

old_val = val; // valor del antiguo estado
if (state==1){ //si el estado es 1 entonces significa que se presionó el botón y se empiezan a leer muestras
  valo=analogRead(A0);
  entrada=(valo*5)/1024;
  Serial.println(entrada);
  delay(10);
}
else{
  valo=0;// apagar
  Serial.println(valo);
  delay(10);

}
}
