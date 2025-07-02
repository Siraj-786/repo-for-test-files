import { User } from "./models";
import { f3 } from "./models";

export function greetUser(u: User): string {
  return u.greet();
}

export const version: string = "1.0.0";

// f1 → f2 → f3 → f4
export function f2() {
  f3();
}
