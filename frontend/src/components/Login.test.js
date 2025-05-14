You have already provided the basic unit test setup for the `onLogin` function. Below are the unit tests for `onCreateAccount` and `onForgotPassword` functions respectively.

```jsx
test('calls onCreateAccount when Create account link is clicked', () => {
  const handleCreateAccount = jest.fn();
  const { getByText } = render(<Login onCreateAccount={handleCreateAccount} />);

  fireEvent.click(getByText(/Create account/i));

  expect(handleCreateAccount).toHaveBeenCalledTimes(1);
});

test('calls onForgotPassword when Forgot Password link is clicked', () => {
  const handleForgotPassword = jest.fn();
  const { getByText } = render(<Login onForgotPassword={handleForgotPassword} />);

  fireEvent.click(getByText(/Forgot Password?/i));

  expect(handleForgotPassword).toHaveBeenCalledTimes(1);
});
```

In these tests, we render the `Login` component with a mock function passed as a prop. Then, we simulate a click on the corresponding link using `fireEvent.click`. Finally, we assert that the mock function was called once when the link was clicked. Note that we use a regular expression to select the link by its text, which makes the test case insensitive and more flexible.