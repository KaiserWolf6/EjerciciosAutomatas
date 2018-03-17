import java.util.Scanner;

public class Automata5 {
	
	char[] car;
	boolean aceptado;
	int cont;

	public void iniciar() {
		cont = 0;
		aceptado = false;
		q0();
	}

	public void q0() {
		System.out.println("q0 es el estado inicial y final");
		aceptado = true;
		if (cont < car.length) {
			if (car[cont] == '0' || car[cont] == '1') {
				cont ++;
				q0();
			}
		}
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Automata5 a = new Automata5();
		System.out.println("Dame una cadena de ceros y/o unos: ");
		String cadena = s.next();
		a.car = cadena.toCharArray();
		a.iniciar();
		if (a.aceptado) 
			System.out.println("La cadena fue aceptada por el automata" + "" + cadena);
		else
			System.out.println("La cadena no fue aceptada por el automa" + "" + cadena);
	}
}