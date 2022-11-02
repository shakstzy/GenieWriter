const TextBox = () => {
	return (
		<div>
			<form>
				<label>
					Word:
					<input type="text" name="rhymeWord" />
				</label>
				<label>
					Artist:
					<input type="text" name="rhymeArtist" />
				</label>
				<input type="Search" value="Search" />
			</form>
		</div>
	);
};

export default TextBox;
