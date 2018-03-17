import java.util.Scanner;

public class Automata2 {
	
	int cont;
	char[] car;
	boolean aceptado;

	public void iniciar() {
		cont = 0;
		aceptado = false;
		q0();
	}

	public void q0() {
		System.out.println("q0 es el estado inicial");
		if (cont < car.length) {
			if (car[cont] == '1') {
				cont ++;
				q1();
			} else if (car[cont] == '0') {
				cont ++;
				q0();
			}
		}
	}

	public void q1() {
		System.out.println("En q1");
		if (cont < car.length) {
			if (car[cont] == '0') {
				cont ++;
				q2();
			} else if (car[cont] == '1') {
				cont ++;
				q1();
			}
		}		
	}

	public void q2() {
		System.out.println("q2 es el estado final");
		aceptado = true;
		if (cont < car.length) {
			if (car[cont] == '1') {
				cont ++;
				q3();
			} else if (car[cont] == '0') {
				cont ++;
				q1();
			}
		}		
	}

	public void q3() {
		System.out.println("En q3");
		if (cont < car.length) {
			if (car[cont] == '1') {
				cont ++;
				qError();
			} else if (car[cont] == '0') {
				cont ++;
				q2();
			}
		}		
	}

	public void qError() {
		System.out.println("Se cicla por siempre esta cadena");
		if (cont < car.length) {
			if (car[cont] == '1') {
				cont ++;
				qError();
			} else if (car[cont] == '0') {
				cont ++;
				qError();
			}
		}		
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Automata2 a = new Automata2();
		System.out.println("Dame una cadena de ceros y unos: ");
		String cadena = s.next();
		a.car = cadena.toCharArray();
		a.iniciar();
		if (a.aceptado) 
			System.out.println("La cadena fue aceptada por el automata" + cadena);
		else
			System.out.println("La cadena no fue aceptada por el automata" + cadena);
	}
}