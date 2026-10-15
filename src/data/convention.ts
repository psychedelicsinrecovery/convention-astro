// The facts of PIR®'s Inaugural Convention, kept in one place so every page tells the same story.
// Sources: psychedelicsinrecovery.org/convention-2026/, the schedule page, and the service site.

export const SITE = "https://www.psychedelicsinrecovery.org";
export const SERVICE = "https://service.psychedelicsinrecovery.org";
export const HUB = "https://psychedelicsinrecovery.github.io";
export const GALLERY_REPO = HUB + "/gallery";
export const PIXIESET =
  "https://pir68.pixieset.com/psychedelicsinrecoverytminauguralconventiondenver2026/";

export const convention = {
  title: "The Inaugural PIR® Convention",
  subtitle: "Psychedelics In Recovery™ – PIR®",
  dates: "October 8–11, 2026",
  venue: "The Alliance Center, Denver, Colorado",
  anniversary:
    "Ten years of PIR®: the fellowship's first gathering, held in its anniversary year.",
  tagline: "Integrating psychedelics into recovery — together, in person at last.",
  photosNote:
    "Photos are shared with the fellowship's consent. If you object to a photo being published, contact Anne R. and it will be removed immediately.",
};

// The four days, as they actually ran. PDF programs are the canonical detail; these cards link to them.
export const days = [
  {
    day: "Thursday",
    date: "October 8",
    label: "Arrivals & evening dinners",
    summary:
      "The fellowship arrives in Denver. Two welcome dinners hosted by trusted servants: Boulder (Avanti Food & Beverage, hosted by Anne R.) and Denver (Denver Milk Market, hosted by Kevin F.).",
    pdf: {
      href: SERVICE + "/wp-content/uploads/2026/10/PIR_Offsite_Agenda_All_Days_-1.pdf",
      label: "Off-site agenda (all days) · PDF",
    },
  },
  {
    day: "Friday",
    date: "October 9",
    label: "Opening day",
    summary:
      "Registration, the Opening Ceremony, and the first panels and groups across the Alliance Center's floors.",
    pdf: {
      href: SITE + "/wp-content/uploads/2026/10/PIR-Convention-Friday-1.pdf",
      label: "Friday program · PDF",
    },
  },
  {
    day: "Saturday",
    date: "October 10",
    label: "Main conference day",
    summary:
      "The fullest day: panels and groups, movement and sound, zen and art, workshops and fellowship on every floor.",
    pdf: {
      href: SERVICE + "/wp-content/uploads/2026/10/PIR_Saturday_Flyer_2.pdf",
      label: "Saturday program · PDF",
    },
  },
  {
    day: "Sunday",
    date: "October 11",
    label: "Closing day",
    summary:
      "Closing panels, the networking dinner, and the fellowship night out at Meow Wolf (7:40–10 PM).",
    pdf: {
      href: SERVICE + "/wp-content/uploads/2026/10/PIR_Sunday_Flyer_2pdf.pdf",
      label: "Sunday program · PDF",
    },
  },
];

// What happened, in plain words. Grows as the write-ups land in the AstroLog.
export const highlights = [
  {
    icon: "cake",
    title: "Ten years, and the first time in one room",
    body: "PIR® turned ten in 2026, and the fellowship gathered in person for the very first time — members from across the country and overseas, many who had only ever known each other through a screen.",
  },
  {
    icon: "book-open",
    title: "A new book was announced",
    body: "\"Living Psychedelic Sober\" was announced at the Convention by the new book subcommittee — a literature milestone for the fellowship, now on the 12-Step pages of the website.",
  },
  {
    icon: "video-camera",
    title: "The whole convention was streamed",
    body: "Every main-session day was streamed to the PIR® YouTube channel so members at home could sit in the circle. The recordings live on the Live Stream page.",
  },
  {
    icon: "hand-heart",
    title: "Scholarships carried people here",
    body: "A virtual pass and a scholarship fund (with an Etheridge Foundation match) meant cost was never the reason to miss the circle.",
  },
  {
    icon: "images",
    title: "The gallery is growing",
    body: "Photos from Denver are being gathered into the fellowship's own gallery — kept on GitHub, free and permanent, credited first name and last initial. Add yours from any browser with the walkthrough.",
  },
  {
    icon: "calendar-blank",
    title: "The story continues in 2027",
    body: "The Inaugural was not a one-off — it was the first page of a tradition. The 2027 Convention is to be announced, and this site will carry its story as it takes shape.",
  },
];

// The ways around, for the cross-links the WordPress hub page and this site share.
export const links = {
  landing: { href: SITE + "/convention-2026/", label: "2026 PIR® Convention", note: "The announcement and event page on psychedelicsinrecovery.org" },
  schedule: { href: SITE + "/convention-2026-schedule/", label: "Schedule & Program", note: "Day cards and printable PDF programs" },
  liveStream: { href: SITE + "/convention-live-stream/", label: "Live Stream", note: "Streaming schedule and the recorded sessions" },
  virtualPass: { href: SITE + "/product/pir-2026-convention-virtual-pass/", label: "Virtual Pass", note: "The at-home pass for the main sessions" },
  committee: { href: SERVICE + "/convention-committee/", label: "Convention Committee", note: "The trusted servants who built this" },
  pixieset: { href: PIXIESET, label: "Convention Photo Gallery", note: "The fellowship's shared album (Pixieset)" },
  youtube: { href: "https://www.youtube.com/@Psychedelicsinrecovery", label: "PIR® on YouTube", note: "Recorded sessions and more" },
  astrolog: { href: HUB + "/changelog-astro-public/", label: "The PIR® AstroLog", note: "The fellowship's public changelog" },
  donate: { href: SITE + "/7th-tradition/", label: "7th Tradition", note: "Keep the fellowship self-supporting" },
  events: { href: SITE + "/events/", label: "Events", note: "The PIR® events calendar" },
};

// Events past and future. Past events keep their record here even as the calendar moves on.
export const events = [
  {
    title: "2026 PIR® Inaugural Convention",
    when: "October 8–11, 2026",
    where: "The Alliance Center, Denver, Colorado",
    status: "past" as const,
    kind: "Convention",
    body: "The first PIR® Convention — four days of panels, groups, workshops, movement and fellowship in the anniversary year. Streamed for members at home; photos gathered into the fellowship gallery.",
    hrefs: [
      { href: SITE + "/convention-2026/", label: "Convention page" },
      { href: SITE + "/convention-2026-schedule/", label: "Schedule" },
      { href: SITE + "/convention-live-stream/", label: "Live stream" },
    ],
  },
  {
    title: "2025 Psychedelic Science Conference",
    when: "June 2025",
    where: "Denver, Colorado",
    status: "past" as const,
    kind: "Presence",
    body: "PIR® held space inside the psychedelic science world — meetings and community for members in recovery attending the conference.",
    hrefs: [{ href: SITE + "/psychedelic-science-conference-2025/", label: "Recap" }],
  },
  {
    title: "The 2027 Convention",
    when: "To be announced",
    where: "To be announced",
    status: "future" as const,
    kind: "Convention",
    body: "The first one was always going to be followed by a second. Watch this page and the announcements for dates and the city.",
    hrefs: [],
  },
];
