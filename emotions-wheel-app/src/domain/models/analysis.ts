export interface AnalysisResult {
    prediction: string,
    score: number[],
}

export interface AnalysisResquest {
    text: string
}