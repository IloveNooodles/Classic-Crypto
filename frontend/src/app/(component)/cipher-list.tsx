import styles from "@/styles/Root.module.scss";
import { description, listOfCipher } from "@/utils/desc";
import { inter } from "@/utils/fonts";
import Link from "next/link";

export default function CipherList({ className }: { className?: string }) {
  return (
    <>
      {listOfCipher.map((cipher: string, index: number) => {
        let slug = cipher.toLowerCase().replaceAll(" ", "-");
        return (
          <Link
            href={`/${slug}`}
            className={className ? styles[className] : styles.card}
            key={index}
          >
            <h2 className={`${inter.className} ${styles.heading}`}>{cipher}</h2>
            <p className={`${inter.className} ${styles.hidden}`}>
              {description[index]}
            </p>
          </Link>
        );
      })}
    </>
  );
}
