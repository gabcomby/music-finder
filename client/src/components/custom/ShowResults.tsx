import type { MatchResults } from "@/schemas/schemas";
import { Button } from "../ui/button";

type ResultsProps = {
  results: MatchResults;
};

const ShowResults = ({ results }: ResultsProps) => {
  return (
    <div className="flex flex-col gap-4">
      <p>Name of the song</p>
      <p>Name of the artist</p>
      <Button variant="outline">Search a new song</Button>
    </div>
  );
};

export default ShowResults;
