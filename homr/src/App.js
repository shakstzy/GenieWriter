// import TextBox from "./components/TextBox"
// const axios = require("axios");
// const users = "http://localhost:3000/users";
import { useEffect, useState } from "react";
import LyricsList from "./components/value.js";
// function App() {
// 	return (
// 		<div className="App">
// 			{/* <TextBox/> */}
// 			<form>
// 				<label>
// 					Word:
// 					<input type="text" name="rhymeWord" />
// 				</label>
// 				<label>
// 					Artist:
// 					<input type="text" name="rhymeArtist" />
// 				</label>
// 				<input type="Search" value="Search" />
// 			</form>
// 		</div>
// 	);
// }

// export default App;

const App = () => {
	const [rhymeWord, setRhymeWord] = useState("");
	const [rhymeArtist, setRhymeArtist] = useState("");
	const rhymeDataArray = [];
	const [rhymeData, setRhymeData] = useState([""]);
	async function fetchLyrics() {
		const url =
			"http://127.0.0.1:5000/serve/" + rhymeArtist + "/" + rhymeWord;
		const response = await fetch(url);
		const lyrics = await response.json();
		return lyrics["body"];
	}

	async function handleSubmit(event) {
		console.log("handleSubmit ran");
		event.preventDefault(); // 👈️ prevent page refresh

		// 👇️ access input values here
		//setRhymeData("");
		console.log("rhymeWord 👉️", rhymeWord);
		console.log("rhymeArtist 👉️", rhymeArtist);
		console.log("rhymeData 👉️", rhymeData);
		const lyrics = await fetchLyrics();
		setRhymeData(lyrics);
		console.log(lyrics);
		console.log("Saif:" + rhymeDataArray);
		// fetch(url)
		// 	.then((response) => response.text())
		// 	.then((data) => setRhymeData(data))
		// 	.then(console.log(rhymeData));
		//console.log(rhymeData);
		// 👇️ clear all input values in the form
	}

	return (
		<div>
			<form onSubmit={handleSubmit}>
				Word
				<input
					id="first_name"
					name="first_name"
					type="text"
					value={rhymeWord}
					onChange={(event) => setRhymeWord(event.target.value)}
				/>
				Artist
				<input
					id="last_name"
					name="last_name"
					type="text"
					value={rhymeArtist}
					onChange={(event) => setRhymeArtist(event.target.value)}
				/>
				<button type="submit">Search</button>
			</form>
			<LyricsList lyrics={rhymeData} />
		</div>
	);
};

export default App;
