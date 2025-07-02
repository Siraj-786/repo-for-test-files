import { User } from "./models";
import { greetUser } from "./utils";
import { f2 } from "./utils";

const u = new User(1, "Alice");
console.log(greetUser(u));

// f1 → f2 → f3 → f4
export function f1() {
    f2();
  }
