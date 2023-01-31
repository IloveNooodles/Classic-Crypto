import { RefObject } from "react";

const key = ["Text", "Number"] as const;
export type availableKeyType = typeof key[number];

export type KeyOptions = {
  text?: string;
  m?: string;
  b?: string;
};

export interface RootForm {
  cipherKey?: KeyOptions;
  text?: RefObject<HTMLTextAreaElement>;
  result?: RefObject<HTMLTextAreaElement>;
  url?: string;
}
