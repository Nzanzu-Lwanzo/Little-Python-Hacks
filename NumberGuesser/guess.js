"user strict";

// Générer le nombre que le joueur devra déviner
const to_guess = Number.parseInt(Math.random()*10)

// Le nombre total d'essais qu'a l'utilisateur
let total_rounds = 10

while (total_rounds > 0) {
	// Démander à l'utilisateur une valeur
	let user_guess = Number.parseInt(prompt("Dévinez la valeur : "))

	// Decrémenter la valeur de total_rounds
	total_rounds--

	// Si les deux valeurs correspondent
	if (total_rounds ==  to_guess) {

		// Il a gagné-On quitte la boucle

		const msg = "Vous avez gagné !"
		// Créer un élément HTML

		const p = document.createElement('p')

		// Lui ajouter ce texte
		p.innerText = msg;

		// Ajouter cet élément au flux de la page
		document.querySelector('d').insertAdjacentHTML("beforeend",p);

		// Afficher aussi dans la console
		console.log(msg)

		// Rompre la boucle
		break
	} else {

		// Le message 
		const msg = "Vous avez perdu ! Tour " + total_rounds

		// Créer un élément HTML
		const p = document.createElement('p')

		// Lui ajouter ce texte
		p.innerText = msg;

		// Ajouter cet élément au flux de la page
		document.querySelector('.d').insertAdjacentHTML("beforeend",p);


		// Afficher aussi dans la console
		console.log(msg)

		// Continuer de redémander des valeurs
		continue
	}
}