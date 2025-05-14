Here's a basic implementation of a Login component:

1. The complete component code:

```jsx
import React, { useState } from "react";
import PropTypes from "prop-types";
import "./Login.css";

function Login({ onLogin, onCreateAccount, onForgotPassword }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onLogin({ username, password });
  };

  return (
    <div className="Login">
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={e => setUsername(e.target.value)}
            required
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />
        </label>
        <button type="submit">Login</button>
      </form>
      <a href="#" onClick={onForgotPassword}>Forgot Password?</a>
      <a href="#" onClick={onCreateAccount}>Create account</a>
    </div>
  );
}

export default Login;
```

2. Any necessary CSS/styling:

```css
/* Login.css */

.Login {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.Login form {
  display: flex;
  flex-direction: column;
  margin-bottom: 1em;
}

.Login form label {
  margin-bottom: 0.5em;
}

.Login form button {
  margin-top: 1em;
}

.Login a {
  margin-top: 0.5em;
}
```

3. PropTypes:

```jsx
Login.propTypes = {
  onLogin: PropTypes.func.isRequired,
  onCreateAccount: PropTypes.func.isRequired,
  onForgotPassword: PropTypes.func.isRequired
};
```

4. Basic unit test setup:

```jsx
import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Login from './Login';

test('calls onLogin with the username and password when submitted', () => {
  const handleLogin = jest.fn();
  const { getByLabelText, getByText } = render(<Login onLogin={handleLogin} />);

  fireEvent.change(getByLabelText(/username/i), { target: { value: 'testuser' } });
  fireEvent.change(getByLabelText(/password/i), { target: { value: 'testpass' } });
  fireEvent.click(getByText(/login/i));

  expect(handleLogin).toHaveBeenCalledWith({ username: 'testuser', password: 'testpass' });
});
```

This component takes three prop functions: `onLogin`, `onCreateAccount`, and `onForgotPassword`. The `onLogin` function is called when the form is submitted, and `onCreateAccount` and `onForgotPassword` are called when the corresponding links are clicked. These functions should handle the actual logic of logging in, creating an account, and resetting a password.