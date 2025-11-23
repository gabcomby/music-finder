import type { SearchResult } from "@/schemas/schemas";
import { Button } from "../ui/button";

type ResultsProps = {
  results: SearchResult;
};

const ShowResults = ({ results }: ResultsProps) => {
  console.log(results);
  return (
    <div className="flex flex-col gap-4">
      <p>{results.song_name}</p>
      <p>Name of the artist</p>
      <Button variant="outline">Search a new song</Button>
    </div>
  );
};

export default ShowResults;
