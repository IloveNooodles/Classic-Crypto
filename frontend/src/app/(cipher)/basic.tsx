"use client";
import ButtonGroup from "@/app/(component)/button-group";
import Key from "@/app/(component)/key";
import styles from "@/styles/Cipher.module.scss";
import { description, listOfCipher } from "@/utils/desc";
import { inter } from "@/utils/fonts";
import { useRef, useState } from "react";
export default function Template({
  name,
  index,
  keyType,
}: {
  name: string;
  index: number;
  keyType: "Text" | "Number";
}) {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [File, setFile] = useState<File | null>(null);

  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <div className={styles.description}>
          <code className={styles.title}>{listOfCipher[index]}</code>
          <p className={inter.className}>{description[index]}</p>
        </div>
        <div className={styles.container}>
          <form className={styles.form}>
            <label htmlFor="input">Input</label>
            <textarea
              name="input"
              className={styles.input}
              placeholder="Place your input here..."
            />
            <Key type={keyType} />
            <label htmlFor="result">Result</label>
            <textarea
              name="result"
              className={styles.input}
              placeholder="The result will come here..."
            />
            <input type="hidden" name={name} />
          </form>
          <ButtonGroup />
        </div>
      </div>
    </main>
  );
}
