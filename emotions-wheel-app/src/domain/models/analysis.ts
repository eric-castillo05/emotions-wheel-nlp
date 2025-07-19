export interface AnalysisResult {
    prediction: string,
    score: number[],
}

export interface AnalysisRequest {
    text: string
}