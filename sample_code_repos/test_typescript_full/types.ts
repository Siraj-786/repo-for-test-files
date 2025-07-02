import { User } from "./models";

export type UserId = keyof User;
export type AdminLevel = "admin" | "superadmin" | "user";

type Props = {
  name: string;
};

export type PropKey = keyof Props;

// f1 → f2 → f3 → f4
export function f4() {
  console.log("Reached final function");
}

