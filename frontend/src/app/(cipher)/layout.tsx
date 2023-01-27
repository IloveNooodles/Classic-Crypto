import "@/app/globals.css";
import { config } from "@fortawesome/fontawesome-svg-core";
import "@fortawesome/fontawesome-svg-core/styles.css";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Link from "next/link";
config.autoAddCss = false;
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <section>
      <head />
      <nav>
        <Link href="/">
          <FontAwesomeIcon icon={faArrowLeft} size="lg" />
        </Link>
      </nav>
      {children}
    </section>
  );
}
