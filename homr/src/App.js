// import TextBox from "./components/TextBox"

import { useState } from "react";

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

	const handleSubmit = (event) => {
		console.log("handleSubmit ran");
		event.preventDefault(); // 👈️ prevent page refresh

		// 👇️ access input values here
		console.log("rhymeWord 👉️", rhymeWord);
		console.log("rhymeArtist 👉️", rhymeArtist);

		// 👇️ clear all input values in the form
		setRhymeWord("");
		setRhymeArtist("");
	};

	return (
		<div>
			<form onSubmit={handleSubmit}>
				Word
				<input
					id="first_name"
					name="first_name"
					type="text"
					onChange={(event) => setRhymeWord(event.target.value)}
					value={rhymeWord}
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
		</div>
	);
};

export default App;
