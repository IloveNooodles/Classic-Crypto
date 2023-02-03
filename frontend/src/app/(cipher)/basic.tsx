"use client";
import ButtonGroup from "@/app/(component)/button-group";
import Key from "@/app/(component)/key";
import styles from "@/styles/Cipher.module.scss";
import { LIST_URL, description, listOfCipher } from "@/utils/desc";
import { inter } from "@/utils/fonts";
import { KeyOptions } from "@/utils/type";
import { useRef, useState } from "react";
export default function Template({
  name,
  index,
  keyType,
  url,
}: {
  name: string;
  index: number;
  keyType: "Text" | "Number";
  url?: string;
}) {
  const textRef = useRef<HTMLTextAreaElement>(null);
  const resultRef = useRef<HTMLTextAreaElement>(null);
  const [key, setKey] = useState<KeyOptions>({});

  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <div className={styles.description}>
          <code className={styles.title}>{listOfCipher[index]}</code>
          <p className={inter.className} style={{ padding: "0.25rem 0" }}>
            {description[index]}
          </p>
        </div>
        <form className={styles.container} encType="multipart/form-data">
          <div className={styles.form}>
            <label htmlFor="text">Input</label>
            <textarea
              name="text"
              className={styles.input}
              placeholder="Place your input here..."
              ref={textRef}
            />
            <Key type={keyType} cipherKey={key} setKey={setKey} />
            <label htmlFor="result">Result</label>
            <textarea
              name="result"
              className={styles.input}
              placeholder="The result will come here..."
              ref={resultRef}
            />
            <input type="hidden" name={name} />
          </div>
          <ButtonGroup
            url={LIST_URL[index]}
            text={textRef}
            result={resultRef}
            cipherKey={key}
          />
        </form>
      </div>
    </main>
  );
}
