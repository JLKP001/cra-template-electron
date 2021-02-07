import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders title", () => {
  render(<App />);
  const title = screen.getByText(/Built using CRA electron-builder Template/i);
  expect(title).toBeInTheDocument();
});
