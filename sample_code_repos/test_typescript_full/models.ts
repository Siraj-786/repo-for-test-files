import { f4 } from "./types";

export class User {
    id: number;
    name: string;
  
    constructor(id: number, name: string) {
      this.id = id;
      this.name = name;
    }
  
    greet(): string {
      return `Hi, I’m ${this.name}`;
    }
  }
  
  export interface IUser {
    id: number;
    name: string;
  }
  
// f1 → f2 → f3 → f4
export function f3() {
  f4();
}