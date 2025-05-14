```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './GameInterface.css';

/**
 * Game Interface Component.
 * This component is responsible for rendering the game layout, sprites and scoreboard.
 * It uses local state to manage the score.
 *
 * @component
 * @example
 * return (
 *   <GameInterface />
 * )
 */
const GameInterface = ({ layout, sprites, scoreboard }) => {
  const [score, setScore] = useState(0);

  const handleScoreChange = (increment) => {
    setScore(score + increment);
  };

  // Error handling for missing props
  if (!layout || !sprites || !scoreboard) {
    return (
      <div className="error">
        Missing one or more required properties: layout, sprites, scoreboard.
      </div>
    );
  }

  return (
    <div className="game-interface">
      <div className="game-layout">{layout}</div>
      <div className="game-sprites">{sprites}</div>
      <div className="game-scoreboard">
        {scoreboard}
        <div className="score">Score: {score}</div>
      </div>
    </div>
  );
};

// PropTypes for Component
GameInterface.propTypes = {
  layout: PropTypes.element.isRequired,
  sprites: PropTypes.element.isRequired,
  scoreboard: PropTypes.element.isRequired,
};

export default GameInterface;
```

CSS:
```css
/* GameInterface.css */

.game-interface {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
}

.game-layout, 
.game-sprites, 
.game-scoreboard {
  margin-bottom: 20px;
}

.score {
  font-size: 20px;
  font-weight: bold;
}
```

Unit Test:
```jsx
import { render } from '@testing-library/react';
import GameInterface from './GameInterface';

test('renders GameInterface component', () => {
  render(<GameInterface layout={<div />} sprites={<div />} scoreboard={<div />} />);
  const layoutElement = screen.getByText(/layout/i);
  expect(layoutElement).toBeInTheDocument();
  
  const spritesElement = screen.getByText(/sprites/i);
  expect(spritesElement).toBeInTheDocument();
  
  const scoreboardElement = screen.getByText(/scoreboard/i);
  expect(scoreboardElement).toBeInTheDocument();
});
```