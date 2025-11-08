import { DateTime } from "luxon";

interface Tag {
  id: number;
  created: DateTime;
  text: string;
}

interface Move {
  id: number;
  tags: Tag[];
  created: DateTime;
  title: string;
  description: string;
}

const fetchMoves = async (): Promise<Move[]> => {
  const response = await fetch("/api/dummy/?format=json", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });

  if (!response.ok) {
    throw new Error(
      `Failed to fetch moves: ${response.status} ${response.statusText}`
    );
  }

  const data: any[] = await response.json();
  return data.map((item) => ({
    id: item.id,
    title: item.title,
    description: item.description,
    created: DateTime.fromISO(item.created),
    tags: item.tags.map(
      (tag: any): Tag => ({
        id: tag.id,
        text: tag.text,
        created: DateTime.fromISO(tag.created),
      })
    ),
  }));
};

export { fetchMoves };
