import React from "react";

const LyricsList = (props) => {
	// console.log(props.lyrics);
	return (
		<div className="users">
			{props.lyrics.map((user) => (
				<div className="user">{user}</div>
			))}
		</div>
	);
};

export default LyricsList;
