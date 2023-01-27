"use client";
import ButtonGroup from "@/app/(component)/button-group";
import Key from "@/app/(component)/key";
import styles from "@/styles/Cipher.module.scss";
import { description } from "@/utils/desc";
import { Inter } from "@next/font/google";
import { useRef, useState } from "react";
const inter = Inter({ subsets: ["latin"] });
export default function Home() {
  const fileRef = useRef<HTMLInputElement>(null);
  const infoRef = useRef<HTMLParagraphElement>(null);
  const [File, setFile] = useState<File | null>(null);

  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <div className={styles.description}>
          <code className={styles.title}>Vigenere Cipher</code>
          <p className={inter.className}>{description[0]}</p>
        </div>
        <div className={styles.container}>
          <form className={styles.form}>
            <label htmlFor="input">Input</label>
            <textarea name="input" className={styles.input} />
            <Key type="Number"/>
            {/* <label htmlFor="Key">Key</label>
            <textarea name="Key" className={`${styles.input} ${styles.key}`} /> */}
            <label htmlFor="result">Result</label>
            <textarea name="result" className={styles.input} />
            <input type="hidden" name="vignere" />
          </form>
          <ButtonGroup />
        </div>
      </div>
    </main>
  );
}
